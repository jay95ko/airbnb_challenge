# Generated by Django 2.2.5 on 2021-05-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_img'),
        ),
    ]
