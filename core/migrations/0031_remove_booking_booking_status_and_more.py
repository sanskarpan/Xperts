# Generated by Django 5.1.1 on 2024-10-04 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_mentor_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='meeting_link',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='schedule',
        ),
    ]
