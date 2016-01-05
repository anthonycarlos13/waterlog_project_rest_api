# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0003_auto_20151225_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set([('name', 'abbreviation')]),
        ),
        migrations.AlterUniqueTogether(
            name='county',
            unique_together=set([('name', 'state_internal')]),
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name', 'abbreviation')]),
        ),
    ]
