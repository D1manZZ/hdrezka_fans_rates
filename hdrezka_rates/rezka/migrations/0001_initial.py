# Generated by Django 3.1.7 on 2021-03-22 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название фильма')),
                ('url', models.CharField(max_length=200, unique=True, verbose_name='Ссылка на фильм')),
                ('image_url', models.CharField(max_length=200, unique=True, verbose_name='Ссылка на картинку')),
                ('genres', models.CharField(max_length=200, verbose_name='Жанры')),
                ('critics_rate', models.FloatField(verbose_name='Оценка на кинопоиске')),
                ('fans_rate', models.FloatField(verbose_name='Оценка зрителей')),
                ('number_of_fans_rate', models.FloatField(verbose_name='Количество оценок зрителей')),
                ('year', models.PositiveIntegerField(verbose_name='Год выпуска')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
    ]
