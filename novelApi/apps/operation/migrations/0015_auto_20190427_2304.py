# Generated by Django 2.2 on 2019-04-27 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0014_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, related_name='favs', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]