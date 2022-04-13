from email.policy import default
from django.utils import timezone
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    sub_title = CharField(max_length=100, verbose_name="Подзаголовок")
    description = models.TextField(verbose_name="Описание")
    date_posted = models.DateTimeField(default=timezone.now)
    image1 = ImageField(default='', upload_to="cart/images",
                        verbose_name="Изображение")


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    email = models.EmailField(max_length=250, verbose_name="майл")
    phone = models.CharField(max_length=100, verbose_name="телефон")
    subject = models.CharField(max_length=100, verbose_name="сообщение")

    contact_info = models.ForeignKey(User, on_delete=models.CASCADE,
                                     null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"


class About(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    sub_title = CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(default='', verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class Postavki(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    sub_title = CharField(max_length=100, verbose_name="Подзаголовок")
    description = models.TextField(verbose_name="Описание")

    image1 = ImageField(default='', upload_to="postavki/images",
                        verbose_name="Изображение1")
    image2 = ImageField(default='', upload_to="postavki/images",
                        verbose_name="Изображение2")
    image3 = ImageField(default='', upload_to="postavki/images",
                        verbose_name="Изображение3")
    image4 = ImageField(default='', upload_to="postavki/images",
                        verbose_name="Изображение4")

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Поставки"
        verbose_name_plural = "Поставки"


class Project(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = ImageField(upload_to="Project/images",
                       verbose_name="Изображение")

    image1 = ImageField(default='', upload_to="projects/images",
                        verbose_name="Изображение1")
    image2 = ImageField(default='', upload_to="projects/images",
                        verbose_name="Изображение2")
    image3 = ImageField(default='', upload_to="projects/images",
                        verbose_name="Изображение3")
    image4 = ImageField(default='', upload_to="projects/images",
                        verbose_name="Изображение4")
    image5 = ImageField(default='', upload_to="projects/images",
                        verbose_name="Изображение5")
    image6 = ImageField(default='', upload_to="projects/images",
                        verbose_name="Изображение6")

    favourites = models.ManyToManyField(
        User, verbose_name='favourites', default=None, blank=True)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"


class Vendor(models.Model):

    image = ImageField(upload_to="portfolio/images",
                       verbose_name="Изображение")
    url = URLField(blank=True, verbose_name="Адрес ссылки")

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = "Вендоры"
        verbose_name_plural = "Вендоры"
