# Generated by Django 2.2 on 2019-04-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_follow_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bgc',
            field=models.URLField(blank=True, default='https://qiniu.tuscanyyy.top/bgc.jpg', help_text='背景', null=True, verbose_name='背景'),
        ),
    ]