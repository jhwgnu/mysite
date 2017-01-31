# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='내용을 입력하세요', verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='제목을 입력하세요', max_length=100, verbose_name='제목'),
        ),
    ]
