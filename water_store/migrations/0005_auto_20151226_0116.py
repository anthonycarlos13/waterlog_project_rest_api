# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0004_auto_20151225_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='state_internal',
            field=models.ForeignKey(to='water_store.State', null=True),
        ),
    ]
