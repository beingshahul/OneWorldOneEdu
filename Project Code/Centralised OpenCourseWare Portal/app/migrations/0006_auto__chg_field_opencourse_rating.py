# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OpenCourse.rating'
        db.alter_column(u'app_opencourse', 'rating', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=1))

    def backwards(self, orm):

        # Changing field 'OpenCourse.rating'
        db.alter_column(u'app_opencourse', 'rating', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=5))

    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'unique': "'true'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.opencourse': {
            'Meta': {'ordering': "['-rating', '-panel_rating', 'title']", 'object_name': 'OpenCourse'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['app.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'panel_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'pubDate': ('django.db.models.fields.DateField', [], {}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '2', 'decimal_places': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Tags']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.tags': {
            'Meta': {'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': "'true'", 'max_length': '100'})
        }
    }

    complete_apps = ['app']