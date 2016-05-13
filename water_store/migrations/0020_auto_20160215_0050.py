# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0019_auto_20160202_0920'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evapotranspiration',
            unique_together=set([('site_code', 'county', 'site_name', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='groundwaterwell',
            unique_together=set([('site_code', 'county', 'site_name', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='precipitation',
            unique_together=set([('site_code', 'county', 'site_name', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='stream',
            unique_together=set([('site_code', 'county', 'site_name', 'date')]),
        ),
    ]
