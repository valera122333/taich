# Generated by Django 4.0.3 on 2022-04-10 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0013_alter_about_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='description',
        ),
    ]
