# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0007_crowd_doc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='GrpExp1',
            new_name='GrpExp1_1',
        ),
        migrations.AddField(
            model_name='questions',
            name='GrpExp1_2',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='GrpExp1_3',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='GrpExp1_4',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='GrpExp1_5',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='GrpExp1_6',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='GrpExp1_7',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
