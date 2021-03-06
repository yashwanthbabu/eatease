# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewdietary',
            name='dairy_rating',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviewdietary',
            name='gluten_rating',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviewdietary',
            name='nuts_rating',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviewdietary',
            name='vegan_rating',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reviewdietary',
            name='vegetarian_rating',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
    ]
