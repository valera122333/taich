# Generated by Django 3.2.9 on 2022-04-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0032_standard_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subject_id',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='standard',
            name='description',
            field=models.TextField(blank=True, max_length=500, verbose_name='описание категории'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='image',
            field=models.ImageField(blank=True, upload_to='standarts/images', verbose_name='изображение категории'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='название категории'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='слаг категории'),
        ),
    ]
