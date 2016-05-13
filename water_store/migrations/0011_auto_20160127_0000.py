# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_store', '0010_reclamationplant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamationplant',
            name='date_recorded',
            field=models.DateTimeField(null=True),
        ),
    ]
