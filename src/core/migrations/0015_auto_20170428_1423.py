# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170428_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 4, 28, 21, 23, 44, 495234, tzinfo=utc), verbose_name='Response received'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='action_link',
            field=models.CharField(blank=True, default='', help_text='This field is only applicable to Action-able opportunities', max_length=255),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='action_text',
            field=models.CharField(blank=True, default='', help_text='This field is only applicable to Action-able opportunities', max_length=255),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='surveys',
            field=models.ManyToManyField(blank=True, help_text='This field is only applicable to Survey-able opportunities', to='core.Survey'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='priority',
            field=models.IntegerField(default=1, help_text='This integer value represents the order                                    in which surveys appear to potential new volunteers.'),
        ),
    ]