# Generated by Django 2.2 on 2020-02-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offre', '0004_auto_20200204_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='offre_done_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='offre',
            name='offre_refuse_date',
            field=models.DateTimeField(null=True),
        ),
    ]
