# Generated by Django 3.2.9 on 2022-04-11 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tehprime', '0022_remove_contact_contact_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
