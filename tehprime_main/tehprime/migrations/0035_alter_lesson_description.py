# Generated by Django 3.2.9 on 2022-04-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0034_lesson_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]