# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141127_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='dairy_rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='gluten_rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='nuts_rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='vegan_rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='vegetarian_rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
