# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StormWater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=4)),
                ('total_annual_rainfall', models.IntegerField(default=0)),
                ('total_annual_rainfall_units', models.CharField(max_length=25)),
                ('annual_change_from_previous_year', models.IntegerField(default=0)),
                ('annual_change_from_average', models.IntegerField(default=0)),
                ('amount_annual_capture', models.IntegerField(default=0)),
                ('amount_annual_capture_units', models.CharField(max_length=5)),
                ('total_capture_per_annum', models.IntegerField(default=0)),
                ('main_source', models.URLField()),
            ],
        ),
    ]
