# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0012_auto_20160127_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamationplant',
            name='reuse_sites',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='reclamationplant',
            name='reuse_sites_sizeACRES',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=4),
        ),
    ]
