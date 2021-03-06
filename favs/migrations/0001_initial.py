# Generated by Django 2.2.5 on 2021-04-19 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('movies', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavList',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('books', models.ManyToManyField(blank=True, to='books.Book')),
                ('movies', models.ManyToManyField(blank=True, to='movies.Movie')),
            ],
            options={
                'verbose_name': 'Favorite List',
            },
        ),
    ]
