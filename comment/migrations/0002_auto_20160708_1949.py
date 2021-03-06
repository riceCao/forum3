# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-08 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='to_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment', verbose_name='被回复评论'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(blank=True, max_length=10000, verbose_name='内容'),
        ),
    ]
