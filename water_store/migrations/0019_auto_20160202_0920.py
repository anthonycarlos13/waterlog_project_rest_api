# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0018_remove_spreadingground_site_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evapotranspiration',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='precipitation',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
