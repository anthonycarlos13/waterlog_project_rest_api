# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0007_auto_20160110_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='groundwaterwell',
            name='site_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='groundwaterwell',
            name='source',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='groundwaterwell',
            name='units',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='groundwaterwell',
            name='value',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=2),
        ),
        migrations.AlterUniqueTogether(
            name='groundwaterwell',
            unique_together=set([('site_code', 'county', 'site_name')]),
        ),
    ]
