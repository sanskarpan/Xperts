# Generated by Django 5.1.1 on 2024-09-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='location',
            field=models.CharField(default='Noida', max_length=255),
        ),
    ]
