from email.policy import default
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
# Create your models here.
from embed_video.fields import EmbedVideoField


class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name='название категории')
    slug = models.SlugField(null=True, blank=True,
                            verbose_name='слаг категории')
    description = models.TextField(
        max_length=500, blank=True, verbose_name='описание категории')
    image = models.ImageField(
        upload_to="standarts/images", blank=True, verbose_name='изображение категории')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Глобальная категория"
        verbose_name_plural = "Глобальная категория"


class Subject(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name='subjects')
    image = models.ImageField(
        upload_to="subject/images", blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегория"


class Lesson(models.Model):

    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=250, verbose_name="Заголовок урока")
    position = models.PositiveSmallIntegerField(verbose_name="Номер урока")
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=5000, blank=True)
    video = EmbedVideoField(default='', verbose_name="ссылка на видео")
    image = models.ImageField(
        upload_to="Lesson/images", blank=True, verbose_name='Subject Image')
    description2 = models.TextField(max_length=5000, blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lesson_list', kwargs={'slug': self.subject.slug, 'standard': self.Standard.slug})

    class Meta:

        verbose_name = "Уроки по музыке"
        verbose_name_plural = "Уроки по музыке"


class Comment(models.Model):
    lesson_name = models.ForeignKey(
        Lesson, null=True, on_delete=models.CASCADE, related_name='comments')
    comm_name = models.CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = (
            "comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']


class Cart(models.Model):
    title = CharField(max_length=100, verbose_name="Заголовок")
    sub_title = CharField(max_length=100, verbose_name="Подзаголовок")
    description = models.TextField(verbose_name="Описание")
    date_posted = models.DateTimeField(default=timezone.now)
    image0 = ImageField(default='', upload_to="cart/images",
                        verbose_name="Изображение на главной")
    image1 = ImageField(default='', upload_to="cart/images",
                        verbose_name="Изображение 1")
    image2 = ImageField(default='', upload_to="cart/images",
                        verbose_name="Изображение2")
    image3 = ImageField(default='', upload_to="cart/images",
                        verbose_name="Изображение3")
    image4 = ImageField(default='', upload_to="cart/images",
                        verbose_name="Изображение4")

    def __str__(self):
        return self.title


STATUS_ZAYZVKA = (

    ('Рассмотрена', 'Рассмотрена'),
    ('В ожидании', 'В ожидании'),
    ('Отклонена', 'Отклонена'),

)


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    email = models.EmailField(max_length=250, verbose_name="майл")
    phone = models.CharField(max_length=100, verbose_name="телефон")
    subject = models.CharField(max_length=100, verbose_name="сообщение")

    contact_info = models.ForeignKey(User, on_delete=models.CASCADE,
                                     null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    status = models.CharField(max_length=30,
                              choices=STATUS_ZAYZVKA, default='Доставлена')

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
