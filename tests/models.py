from django.db import models
from django.contrib.auth.models import User
from learning.models import Lecture


class TestProfile(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва тесту')
    work_time = models.IntegerField(verbose_name='Час на виконання (хв)')
    questions_count = models.IntegerField(verbose_name='Кількість запитань', blank=True, null=True)
    statisfactory = models.IntegerField(verbose_name='Задовільно')
    good = models.IntegerField(verbose_name='Добре')
    perfect = models.IntegerField(verbose_name='Відмінно')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тести'

    def __str__(self):
        return self.name


class Question(models.Model):
    ProfileId = models.ForeignKey(TestProfile, on_delete=models.CASCADE, verbose_name='Тест')
    text = models.TextField(verbose_name='Текст питання')
    weight = models.FloatField(default=1)

    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'

    def __str__(self):
        return self.text


class Answer(models.Model):
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    isRight = models.BooleanField()

    class Meta:
        verbose_name = 'Варіант відповіді'
        verbose_name_plural = 'Варіанти відповіді'

    def __str__(self):
        return self.text


class Result(models.Model):
    ProfileId = models.ForeignKey(TestProfile, on_delete=models.CASCADE, verbose_name='Тест')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    time_finished = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Час завершення")
    rating = models.FloatField(verbose_name="відсоток")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результати'
