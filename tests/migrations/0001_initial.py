# Generated by Django 4.2.1 on 2023-05-23 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('learning', '0002_alter_course_options_remove_course_text_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва тесту')),
                ('work_time', models.IntegerField(verbose_name='Час на виконання (хв)')),
                ('questions_count', models.IntegerField(blank=True, null=True, verbose_name='Кількість запитань')),
                ('statisfactory', models.IntegerField(verbose_name='Задовільно')),
                ('good', models.IntegerField(verbose_name='Добре')),
                ('perfect', models.IntegerField(verbose_name='Відмінно')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.lecture')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тести',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_finished', models.DateTimeField(auto_now_add=True, verbose_name='Час завершення')),
                ('rating', models.FloatField(verbose_name='відсоток')),
                ('ProfileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testprofile', verbose_name='Тест')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результати',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст питання')),
                ('weight', models.FloatField(default=1)),
                ('ProfileId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testprofile', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Питання',
                'verbose_name_plural': 'Питання',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('isRight', models.BooleanField()),
                ('QuestionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.question')),
            ],
            options={
                'verbose_name': 'Варіант відповіді',
                'verbose_name_plural': 'Варіанти відповіді',
            },
        ),
    ]
