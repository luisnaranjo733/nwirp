# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_merge_20170428_2128'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='QuestionResponse',
        ),
    ]
