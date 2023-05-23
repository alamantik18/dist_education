# Generated by Django 4.2.1 on 2023-05-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва курсу')),
                ('text', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('mark', models.FloatField()),
                ('description', models.CharField(max_length=250, verbose_name='Опис курсу')),
                ('preview_image', models.ImageField(upload_to='media/courses_preview')),
            ],
        ),
    ]
