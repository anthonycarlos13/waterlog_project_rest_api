# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('abbreviation', models.CharField(max_length=5, null=True, blank=True)),
                ('country_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('county_code', models.IntegerField(default=0)),
                ('active_status', models.CharField(max_length=5, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True, null=True, blank=True)),
                ('abbreviation', models.CharField(max_length=10, unique=True, null=True, blank=True)),
                ('state_code', models.IntegerField(default=0)),
                ('country', models.ForeignKey(blank=True, to='water_store.Country', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='county',
            name='state',
            field=models.ForeignKey(blank=True, to='water_store.State', null=True),
        ),
    ]
