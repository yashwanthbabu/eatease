# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('address', models.CharField(max_length=128)),
                ('postcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=14)),
                ('coords', models.CharField(max_length=24)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RestaurantMenus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nuts_marked', models.BooleanField(default=False)),
                ('nuts_sep', models.BooleanField(default=False)),
                ('gluten_marked', models.BooleanField(default=False)),
                ('gluten_sep', models.BooleanField(default=False)),
                ('vegetarian_marked', models.BooleanField(default=False)),
                ('vegetarian_sep', models.BooleanField(default=False)),
                ('vegan_marked', models.BooleanField(default=False)),
                ('vegan_sep', models.BooleanField(default=False)),
                ('dairy_marked', models.BooleanField(default=False)),
                ('dairy_sep', models.BooleanField(default=False)),
                ('general_sep', models.BooleanField(default=False)),
                ('restaurant', models.OneToOneField(to='main.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('overall_text', models.TextField(max_length=2056)),
                ('overall_rating', models.PositiveSmallIntegerField()),
                ('restaurant', models.ForeignKey(to='main.Restaurant')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewDietary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nuts_rating', models.PositiveSmallIntegerField(default=0)),
                ('gluten_rating', models.PositiveSmallIntegerField(default=0)),
                ('vegetarian_rating', models.PositiveSmallIntegerField(default=0)),
                ('vegan_rating', models.PositiveSmallIntegerField(default=0)),
                ('dairy_rating', models.PositiveSmallIntegerField(default=0)),
                ('review', models.OneToOneField(to='main.Review')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
