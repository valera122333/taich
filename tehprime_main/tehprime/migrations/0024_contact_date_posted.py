# Generated by Django 3.2.9 on 2022-04-11 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0023_contact_contact_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]