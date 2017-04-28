# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_opportunity_opportunity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='opportunity_type',
            field=models.CharField(choices=[('Action-able', 'Action-able'), ('Survey-able', 'Survey-able')], default='Survey-able', max_length=32),
        ),
    ]