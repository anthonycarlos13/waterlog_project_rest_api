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
            name='Evapotranspiration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=100, null=True)),
                ('site_code', models.CharField(max_length=100, null=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('date', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField()),
                ('value', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('units', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(max_length=500, null=True)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroundWaterWell',
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
        migrations.CreateModel(
            name='Precipitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=100, null=True)),
                ('site_code', models.CharField(max_length=100, null=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('date', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField()),
                ('value', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('units', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(max_length=500, null=True)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReclamationPlant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(max_length=100, null=True)),
                ('treatment_type', models.CharField(max_length=100, null=True)),
                ('capacity_MGD', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('water_producedMGD', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('date_recorded', models.DateTimeField(null=True)),
                ('water_producedAFY', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('operation_management_costAFY', models.CharField(max_length=20, null=True)),
                ('operation_management_costY', models.CharField(max_length=20, null=True)),
                ('water_reusedMGD', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('water_reusedAFY', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('reuse_sites', models.DecimalField(null=True, max_digits=20, decimal_places=4)),
                ('reuse_sites_sizeACRES', models.DecimalField(null=True, max_digits=20, decimal_places=4)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservoir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dam_id', models.CharField(max_length=10, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('reservoir_elevation', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('reservoir_storage', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('reservoir_area', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=3, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=3, blank=True)),
                ('county', models.CharField(max_length=100, null=True, blank=True)),
                ('stream', models.CharField(max_length=100, null=True, blank=True)),
                ('storage_capacity', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('outflow', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('inflow', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('precipitation_incremental', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('precipitation_accumulated', models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('source', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpreadingGround',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=100, null=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('area', models.CharField(max_length=100, null=True)),
                ('percolation', models.CharField(max_length=75, null=True)),
                ('storage', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('units', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(max_length=500, null=True)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('abbreviation', models.CharField(max_length=10, null=True, blank=True)),
                ('state_code', models.IntegerField(default=0)),
                ('country_internal', models.ForeignKey(blank=True, to='water_store.Country', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=100, null=True)),
                ('site_code', models.CharField(max_length=100, null=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=6)),
                ('date', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField()),
                ('value', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('units', models.CharField(max_length=100, null=True)),
                ('source', models.CharField(max_length=500, null=True)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='reservoir',
            unique_together=set([('id', 'date')]),
        ),
        migrations.AddField(
            model_name='county',
            name='state_internal',
            field=models.ForeignKey(to='water_store.State', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set([('name', 'abbreviation')]),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'abbreviation')]),
        ),
        migrations.AlterUniqueTogether(
            name='county',
            unique_together=set([('name', 'state_internal')]),
        ),
    ]
