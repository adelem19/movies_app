# Generated by Django 3.2 on 2022-01-16 16:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Актёры и Режиссёры',
                'verbose_name_plural': 'Актёры и Режиссёры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Жанр')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назавние')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2022, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('world_premire', models.DateField(default=datetime.date.today, verbose_name='Премьера в мире')),
                ('budget', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в США')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='Указывать сумму в долларах', verbose_name='Сборы в Мире')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=True, verbose_name='Черновик')),
                ('actors', models.ManyToManyField(related_name='film_actors', to='films.Actor', verbose_name='Актёры')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.category', verbose_name='Катугория')),
                ('directors', models.ManyToManyField(related_name='film_director', to='films.Actor', verbose_name='Режиссёр')),
                ('genre', models.ManyToManyField(to='films.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звёзда рейтинга',
                'verbose_name_plural': 'Звёзды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie', verbose_name='Фильм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.reviews', verbose_name='Ролитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie', verbose_name='Фильм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтиг',
                'verbose_name_plural': 'Рейтиги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Кадр из фильма',
                'verbose_name_plural': 'Кадры из фильма',
            },
        ),
    ]
