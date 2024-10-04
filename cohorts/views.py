from rest_framework import viewsets,status
from .models import Cohort, CohortRegistration, Payment
from .serializers import CohortSerializer, CohortRegistrationSerializer, PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import hmac
from razorpay import Client
from django.conf import settings
import hashlib

# Initialize the Razorpay client with your API key and secret
razorpay_client = Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer

class CohortRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CohortRegistration.objects.all()
    serializer_class = CohortRegistrationSerializer

    def create(self, request, *args, **kwargs):
        cohort = Cohort.objects.get(id=request.data.get('cohort'))
        registration = CohortRegistration.objects.create(
            user=request.user,
            cohort=cohort,
            payment_status='Pending'
        )
        
        # Create a Razorpay order
        razorpay_order = razorpay_client.order.create({
            "amount": int(cohort.price * 100),  # Amount in paisa
            "currency": "INR",
            "receipt": str(registration.id),
            "payment_capture": 1
        })

        # Save the payment with the razorpay_order_id
        payment = Payment.objects.create(
            user=request.user,
            cohort_registration=registration,
            amount=cohort.price,
            razorpay_order_id=razorpay_order['id']
        )

        return Response({
            "registration_id": registration.id,
            "razorpay_order_id": razorpay_order['id'],
            "amount": cohort.price
        }, status=status.HTTP_201_CREATED)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def update(self, request, *args, **kwargs):
        payment = self.get_object()

        # Ensure that the Razorpay details including the signature are stored
        payment.razorpay_payment_id = request.data.get('razorpay_payment_id')
        payment.razorpay_signature = request.data.get('razorpay_signature')
        payment.payment_status = 'Success' if request.data.get('status') == 'Success' else 'Failed'
        payment.save()

        if payment.payment_status == 'Success':
            payment.cohort_registration.payment_status = 'Completed'
            payment.cohort_registration.razorpay_signature = 'razorpay_signature'
            payment.cohort_registration.save()

        return Response({"status": "Payment status updated and signature stored."})


class PaymentVerificationViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        payment_id = request.data.get('razorpay_payment_id')
        order_id = request.data.get('razorpay_order_id')
        signature = request.data.get('razorpay_signature')

        payment = Payment.objects.get(razorpay_order_id=order_id)

        # Generate the signature using the payment details
        generated_signature = hmac.new(
            key=settings.RAZORPAY_API_SECRET.encode(),
            msg=(order_id + "|" + payment_id).encode(),
            digestmod=hashlib.sha256
        ).hexdigest()

        if generated_signature == signature:
            payment.verified = True
            payment.payment_status = 'Success'
            payment.cohort_registration.payment_status = 'Completed'
            payment.cohort_registration.save()
            payment.save()

            return Response({"status": "Payment verified and registration completed."}, status=status.HTTP_200_OK)
        else:
            payment.payment_status = 'Failed'
            payment.save()
            return Response({"status": "Payment verification failed."}, status=status.HTTP_400_BAD_REQUEST)
