# Generated by Django 2.2 on 2019-04-19 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_auto_20190418_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmt',
            name='reply',
            field=models.ForeignKey(help_text='回复: 空(评论), 非空(回复)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replys', to='operation.Cmt', verbose_name='回复'),
        ),
    ]