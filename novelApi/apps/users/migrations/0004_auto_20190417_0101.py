# Generated by Django 2.2 on 2019-04-17 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190417_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(blank=True, default='http://qiniu.tuscanyyy.top/avatar', help_text='头像', null=True, verbose_name='头像'),
        ),
    ]
