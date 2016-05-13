# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0011_auto_20160127_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamationplant',
            name='operation_management_costAFY',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reclamationplant',
            name='operation_management_costY',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
