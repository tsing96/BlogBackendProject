# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-16 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180616_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articledetail',
            name='language',
            field=models.CharField(blank=True, choices=[('CN', '中文'), ('EN', 'English')], help_text='现暂时提供两种语言类别', max_length=5, null=True, verbose_name='文章详情语言类别'),
        ),
    ]
