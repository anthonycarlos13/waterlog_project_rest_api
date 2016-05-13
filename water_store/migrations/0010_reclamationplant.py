# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0009_auto_20160118_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReclamationPlant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(max_length=100, null=True)),
                ('treatment_type', models.CharField(max_length=100, null=True)),
                ('capacity_MGD', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('water_producedMGD', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('date_recorded', models.DateTimeField(auto_now=True, null=True)),
                ('water_producedAFY', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('operation_management_costAFY', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('operation_management_costY', models.DecimalField(null=True, max_digits=18, decimal_places=2)),
                ('water_reusedMGD', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('water_reusedAFY', models.DecimalField(null=True, max_digits=75, decimal_places=4)),
                ('reuse_sites', models.IntegerField(default=0, null=True)),
                ('reuse_sites_sizeACRES', models.IntegerField(default=0, null=True)),
                ('county', models.ForeignKey(to='water_store.County', null=True)),
            ],
        ),
    ]
