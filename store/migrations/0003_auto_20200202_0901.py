# Generated by Django 2.2 on 2020-02-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200116_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre_book',
            field=models.ManyToManyField(to='store.Genre'),
        ),
    ]
