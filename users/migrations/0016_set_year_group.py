# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_set_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='year_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.YearGroup'),
            preserve_default=False,
        ),
    ]
