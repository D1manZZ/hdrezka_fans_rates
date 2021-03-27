from django.db import models


class Films(models.Model):

    title = models.CharField('Название фильма', max_length=50)
    url = models.CharField('Ссылка на фильм', max_length=200)
    image_url = models.CharField('Ссылка на картинку', max_length=200)
    genres = models.CharField('Жанры', max_length=200)
    critics_rate = models.FloatField('Оценка на кинопоиске')
    fans_rate = models.FloatField('Оценка зрителей')
    number_of_fans_rate = models.PositiveIntegerField('Количество оценок зрителей')
    year = models.IntegerField('Год выпуска', default=1)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Genres(models.Model):

    genre = models.CharField('Жанр', max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre