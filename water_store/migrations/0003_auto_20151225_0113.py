# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0002_auto_20151224_0307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='county',
            old_name='state',
            new_name='state_internal',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='country',
            new_name='country_internal',
        ),
    ]
