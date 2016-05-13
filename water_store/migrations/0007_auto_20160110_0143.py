# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0006_auto_20160105_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groundwaterwell',
            old_name='date_requested',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='groundwaterwell',
            name='date_last_updated',
        ),
        migrations.RemoveField(
            model_name='groundwaterwell',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='groundwaterwell',
            name='start_date',
        ),
    ]
