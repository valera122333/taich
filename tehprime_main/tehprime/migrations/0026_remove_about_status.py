# Generated by Django 3.2.9 on 2022-04-13 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0025_about_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='status',
        ),
    ]
