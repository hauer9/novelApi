# Generated by Django 2.2 on 2019-04-26 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0012_auto_20190426_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='novel',
            field=models.ForeignKey(help_text='作品', on_delete=django.db.models.deletion.CASCADE, to='novels.Novel', verbose_name='作品'),
        ),
    ]
