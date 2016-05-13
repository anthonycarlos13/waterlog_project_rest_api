# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0013_auto_20160127_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groundwaterwell',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='groundwaterwell',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=75, decimal_places=6),
        ),
    ]
