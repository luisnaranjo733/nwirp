# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 09:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='manager',
            field=models.ManyToManyField(to='core.Manager'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]