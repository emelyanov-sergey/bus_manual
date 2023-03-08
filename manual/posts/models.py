from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Группа')
    slug = models.SlugField(unique=True, verbose_name='Путь')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=250)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Группа',
        help_text='Группа'
    )
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})
