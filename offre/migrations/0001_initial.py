# Generated by Django 2.2 on 2020-01-06 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('state', models.CharField(default='waiting for response', max_length=100)),
                ('usedbookoffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offreusedbookoffer', to='store.Usedbook')),
                ('userdemandeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offreuserdemandeur', to=settings.AUTH_USER_MODEL)),
                ('useroffreur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offreuseroffreur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]