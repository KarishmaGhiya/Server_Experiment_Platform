# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 18:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20160620_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='Statement',
            new_name='statement',
        ),
    ]
