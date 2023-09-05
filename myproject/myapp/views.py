import logging

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    about_html = """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Index-DjangoFramework</title>
  <style>
    h1, h2 {
    font-family: Geneva, Arial, Helvetica, sans-serif;
   }
   p, ul {
    font-family: Geneva, Arial, Helvetica, sans-serif;
   }
  </style>
</head>
<body>
<h1>Hello, world!</h1>

<p>Навигация по сайту:<br> 
<ul> 
    <li>http://127.0.0.1:8000 - page&nbsp;&laquo;<strong>Index</strong>&raquo;(текущая)</li>
    <li>http://127.0.0.1:8000/about - page&nbsp;&laquo;<strong>About&nbsp;</strong>&raquo;</li>  
    <li>http://127.0.0.1:8000/main - page&nbsp;&laquo;<strong>Main</strong>&raquo;</li>         
    <li>http://127.0.0.1:8000/about_me - page&nbsp;&laquo;<strong>About&nbsp;me</strong>&raquo;</li>
    <li>http://127.0.0.1:8000/games/heads_or_tails</li>
    <li>http://127.0.0.1:8000/games/playing_cube_face</li>
    <li>http://127.0.0.1:8000/games/random_number</li>
</ul>
</p>
</body>
</html>
    """
    return HttpResponse(about_html)


def main(request):
    logger.info('Main page accessed')
    main_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Main-DjangoFramework</title>
  <style>
    h1, h2 {
    font-family: Geneva, Arial, Helvetica, sans-serif;
   }
   p, ul {
    font-family: Geneva, Arial, Helvetica, sans-serif;
   }
  </style>
</head>
<body>
<h1>Сайт по изучению Django</h1>

<h2>Что такое Django?</h2>
<p>Django - это высокоуровневый фреймворк для веб-приложений на языке Python. Он был создан в 2005 году и с тех пор
активно развивается и обновляется сообществом разарботчиков по всему миру.</p>

<h2>Обзор фреймворка Django</h2>
<p>Django предоставляет разработчикам множество инструментов и функций для создания веб-приложений, таких как:<br>
  <ul>
    <li>ORM (Object-Relational Mapping)  для работы с базами данных</li>
    <li>URL-маршрутизация</li>
    <li>Аутентификация и авторизация пользователей</li>
    <li>Шаблонизация</li>
    <li>Кеширование</li>
    <li>Интернационализация</li>
    <li>Административная панель</li>
  </ul>
</p>

 <h2>Преимущества исползования Django</h2>
<p>Использование Django имеет множество преимуществ, таких как:
  <ul>
  <li>Быстрая разработка веб-приложений</li>
  <li>Простота и удоство использования</li>
  <li>Высокая производителность</li>
  <li>Безопасность</li>
  <li>Масштабируемость</li>
  </ul>
</p>

</body>
</html>
    """
    return HttpResponse(main_html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse("About us")


def about_me(request):
    logger.info('About_me page accessed')
    about_me_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>About me-DjangoFramework</title>
  <style>
    h1, h2 {
    font-family: Geneva, Arial, Helvetica, sans-serif;
   }
   p, ul {
    font-family: Geneva, Arial, Helvetica, sans-serif;
   }
  </style>
</head>
<body>
<h1>О себе</h1>

<p>Факультет</p>
<h2>Разработчик - Веб-разработка на Python. Технологическая спциализация</h2>
<p>
  Группа: <strong>4071</strong><br><br>
  Студент: Андрей Милых
</p>
</body>
</html>
    """
    return HttpResponse(about_me_html)
