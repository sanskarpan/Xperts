# Generated by Django 5.1.1 on 2024-10-03 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorbooking', '0002_alter_booking_availability_alter_booking_mentor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='booking',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
