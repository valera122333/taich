# Generated by Django 3.2.9 on 2022-04-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0028_auto_20220425_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.AddField(
            model_name='standard',
            name='image',
            field=models.ImageField(blank=True, upload_to='guides/images', verbose_name='Subject Image'),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]