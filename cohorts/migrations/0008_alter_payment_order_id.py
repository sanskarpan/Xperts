# Generated by Django 5.0 on 2024-08-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0007_payment_order_id_alter_payment_razorpay_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_id',
            field=models.CharField(default='TEMP', editable=False, max_length=10),
        ),
    ]
