from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назва курсу')
    published = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    mark = models.FloatField()
    description = models.CharField(max_length=250, verbose_name='Опис курсу')
    preview_image = models.ImageField(upload_to='media/courses_preview')
    lecturer = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Створити курс'
        verbose_name_plural = 'Курси'

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва лекції')
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    preview_image = models.ImageField(upload_to='media/lecture_preview')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Створити лекційний матеріал'
        verbose_name_plural = 'Лекційні матеріали'

    def __str__(self):
        return self.title