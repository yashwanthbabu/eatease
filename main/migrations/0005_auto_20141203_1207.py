# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20141128_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='coords',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.DecimalField(default=0, max_digits=13, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lng',
            field=models.DecimalField(default=0, max_digits=13, decimal_places=10),
            preserve_default=True,
        ),
    ]
