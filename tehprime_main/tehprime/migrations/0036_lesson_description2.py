# Generated by Django 3.2.9 on 2022-04-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0035_alter_lesson_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='description2',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
