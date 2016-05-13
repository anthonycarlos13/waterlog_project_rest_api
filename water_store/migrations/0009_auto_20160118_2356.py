# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0008_auto_20160118_0318'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groundwaterwell',
            unique_together=set([]),
        ),
    ]
