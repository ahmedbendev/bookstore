# Generated by Django 2.2 on 2020-02-04 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('offre', '0003_auto_20200202_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='offre_aprove_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='offre',
            name='offre_pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]