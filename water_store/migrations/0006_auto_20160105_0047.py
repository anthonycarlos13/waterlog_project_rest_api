# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0005_auto_20151226_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroundWaterWell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_code', models.CharField(max_length=100, null=True)),
                ('latitude', models.DecimalField(null=True, max_digits=75, decimal_places=2)),
                ('longitude', models.DecimalField(null=True, max_digits=75, decimal_places=2)),
                ('date_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('date_requested', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField()),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='groundwaterwell',
            unique_together=set([('site_code', 'county')]),
        ),
    ]
