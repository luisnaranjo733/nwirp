# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_response_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]
