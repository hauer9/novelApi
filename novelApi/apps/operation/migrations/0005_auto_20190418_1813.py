# Generated by Django 2.2 on 2019-04-18 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20190418_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmt',
            name='root',
        ),
        migrations.AlterField(
            model_name='cmt',
            name='reply',
            field=models.ForeignKey(help_text='回复: 空(评论), 非空(回复)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_user', to='operation.Cmt', verbose_name='回复'),
        ),
    ]
