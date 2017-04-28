# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170428_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='action_link',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='action_text',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='surveys',
            field=models.ManyToManyField(blank=True, help_text='Surveys for Action-able                                      opportunities will not be issued to                                      potential new volunteers. ', to='core.Survey'),
        ),
    ]