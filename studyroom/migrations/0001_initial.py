# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-25 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sroom1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved', models.DateTimeField()),
                ('name1', models.TextField()),
                ('sid1', models.TextField()),
                ('name2', models.TextField()),
                ('sid2', models.TextField()),
            ],
        ),
    ]
