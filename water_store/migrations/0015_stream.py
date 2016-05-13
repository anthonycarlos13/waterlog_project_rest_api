# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0014_auto_20160127_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=100, null=True)),
                ('site_code', models.CharField(max_length=100, null=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField()),
                ('value', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('units', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(max_length=500, null=True)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
    ]
