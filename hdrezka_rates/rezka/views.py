from django.shortcuts import redirect
from django.views.generic import ListView
from .models import *

import requests
from bs4 import BeautifulSoup


class FilmsList(ListView):
    queryset = Films.objects.filter(fans_rate__gte=9).filter(genres__contains='Фантастика').filter(number_of_fans_rate__gte=500).filter(year__gte=2008).order_by('fans_rate')
    # queryset = Films.objects.filter(fans_rate__gte=9.6).filter(number_of_fans_rate__gte=300).order_by('fans_rate')
    template_name = 'rezka/list.html'
    context_object_name = 'films'


def update_films(request):

    url = 'https://rezka.ag/films/best/page/'
    films_urls = []
    list_of_films = []

    for i in range(1, 597):
        response = requests.get(f'{url}{i}/')
        data = BeautifulSoup(response.text, features="html.parser")
        film_block = data.findAll('div', class_='b-content__inline_item')
        for j in film_block:
            films_urls.append(j['data-url'])

    for i in films_urls:
        film_data = {}
        response = requests.get(i)
        data = BeautifulSoup(response.text, features="html.parser")
        film_data['title'] = data.find(itemprop='name').text
        film_data['url'] = i
        try:
            film_data['image_url'] = data.find('img', itemprop='image')['src']
        except:
            film_data['image_url'] = 'https://cdn0.iconfinder.com/data/icons/shift-free/32/Error-512.png'
        try:
            film_data['genres'] = ", ".join(j.text for j in data.findAll('span', itemprop='genre'))
        except:
            film_data['genres'] = ''
        try:
            film_data['critics_rate'] = float(data.find('span', class_='kp').find('span', class_='bold').text)
        except:
            film_data['critics_rate'] = 1
        try:
            film_data['fans_rate'] = float(data.find('span', itemprop='average').text)
        except:
            film_data['fans_rate'] = 1
        try:
            film_data['number_of_fans_rate'] = int(data.find('span', itemprop='votes').text)
        except:
            film_data['number_of_fans_rate'] = 1
        try:
            film_data['year'] = int(
                data.find('h2', text='Дата выхода').parent.parent.contents[3].find('a').text.split(' ')[0])
        except:
            film_data['year'] = 1
        list_of_films.append(film_data)

    Films.objects.all().delete()

    for i in list_of_films:
        obj = Films(title=i['title'], url=i['url'], image_url=i['image_url'], genres=i['genres'], critics_rate=i['critics_rate'],
        fans_rate = i['fans_rate'], number_of_fans_rate=i['number_of_fans_rate'], year=i['year'])
        obj.save()

    return redirect('films')
