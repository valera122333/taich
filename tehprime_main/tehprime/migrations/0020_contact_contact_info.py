# Generated by Django 3.2.9 on 2022-04-11 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tehprime', '0019_project_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_info',
            field=models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL, verbose_name='contact_info'),
        ),
    ]