# Generated by Django 3.2.6 on 2021-10-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstore',
            name='book_cover',
            field=models.URLField(max_length=400, verbose_name='Book Cover'),
        ),
    ]