# Generated by Django 4.0.3 on 2022-04-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0012_project_image5_project_image6_alter_project_image4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.CharField(max_length=2500, verbose_name='Описание'),
        ),
    ]
