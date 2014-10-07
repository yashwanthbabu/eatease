# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Restaurant'
        db.create_table('core_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('coords', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('core', ['Restaurant'])

        # Adding model 'RestaurantMenus'
        db.create_table('core_restaurantmenus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Restaurant'])),
            ('nuts_marked', self.gf('django.db.models.fields.BooleanField')()),
            ('nuts_sep', self.gf('django.db.models.fields.BooleanField')()),
            ('gluten_marked', self.gf('django.db.models.fields.BooleanField')()),
            ('gluten_sep', self.gf('django.db.models.fields.BooleanField')()),
            ('vegetarian_marked', self.gf('django.db.models.fields.BooleanField')()),
            ('vegetarian_sep', self.gf('django.db.models.fields.BooleanField')()),
            ('vegan_marked', self.gf('django.db.models.fields.BooleanField')()),
            ('vegan_sep', self.gf('django.db.models.fields.BooleanField')()),
            ('dairy_marked', self.gf('django.db.models.fields.BooleanField')()),
            ('dairy_sep', self.gf('django.db.models.fields.BooleanField')()),
            ('general_sep', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('core', ['RestaurantMenus'])

        # Adding model 'Review'
        db.create_table('core_review', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Restaurant'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('overall_text', self.gf('django.db.models.fields.TextField')(max_length=2056)),
            ('overall_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('core', ['Review'])

        # Adding model 'ReviewDietary'
        db.create_table('core_reviewdietary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['core.Review'])),
            ('nuts_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('gluten_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('vegetarian_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('vegan_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('dairy_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['ReviewDietary'])


    def backwards(self, orm):
        # Deleting model 'Restaurant'
        db.delete_table('core_restaurant')

        # Deleting model 'RestaurantMenus'
        db.delete_table('core_restaurantmenus')

        # Deleting model 'Review'
        db.delete_table('core_review')

        # Deleting model 'ReviewDietary'
        db.delete_table('core_reviewdietary')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'coords': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.restaurantmenus': {
            'Meta': {'object_name': 'RestaurantMenus'},
            'dairy_marked': ('django.db.models.fields.BooleanField', [], {}),
            'dairy_sep': ('django.db.models.fields.BooleanField', [], {}),
            'general_sep': ('django.db.models.fields.BooleanField', [], {}),
            'gluten_marked': ('django.db.models.fields.BooleanField', [], {}),
            'gluten_sep': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nuts_marked': ('django.db.models.fields.BooleanField', [], {}),
            'nuts_sep': ('django.db.models.fields.BooleanField', [], {}),
            'restaurant': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Restaurant']"}),
            'vegan_marked': ('django.db.models.fields.BooleanField', [], {}),
            'vegan_sep': ('django.db.models.fields.BooleanField', [], {}),
            'vegetarian_marked': ('django.db.models.fields.BooleanField', [], {}),
            'vegetarian_sep': ('django.db.models.fields.BooleanField', [], {})
        },
        'core.review': {
            'Meta': {'object_name': 'Review'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'overall_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'overall_text': ('django.db.models.fields.TextField', [], {'max_length': '2056'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Restaurant']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'core.reviewdietary': {
            'Meta': {'object_name': 'ReviewDietary'},
            'dairy_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'gluten_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nuts_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'review': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['core.Review']"}),
            'vegan_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'vegetarian_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['core']