# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-20 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brew', '0002_auto_20180420_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewinfo',
            name='bean_text',
            field=models.CharField(max_length=50, verbose_name='咖啡豆'),
        ),
    ]