# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservoir',
            name='county',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='dam_id',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='inflow',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='outflow',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='precipitation_accumulated',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='precipitation_incremental',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='reservoir_area',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='reservoir_elevation',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='reservoir_storage',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='source',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='storage_capacity',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='reservoir',
            name='stream',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
