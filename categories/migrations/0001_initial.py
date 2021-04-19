# Generated by Django 2.2.5 on 2021-04-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('kind', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie'), ('both', 'Both')], max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
