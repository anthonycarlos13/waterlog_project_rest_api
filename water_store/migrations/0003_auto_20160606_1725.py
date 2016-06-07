# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0002_auto_20160606_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservoir',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
