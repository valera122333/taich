# Generated by Django 3.2.9 on 2022-04-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0031_comment_lesson_standard_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='image',
            field=models.ImageField(blank=True, upload_to='standarts/images', verbose_name='Subject Image'),
        ),
    ]
