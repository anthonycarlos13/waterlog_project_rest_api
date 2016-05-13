# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0017_spreadingground'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spreadingground',
            name='site_code',
        ),
    ]
