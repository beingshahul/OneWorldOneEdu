# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OpenCourse.rating'
        db.add_column(u'app_opencourse', 'rating',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=5),
                      keep_default=False)

        # Adding field 'OpenCourse.panelrating'
        db.add_column(u'app_opencourse', 'panelrating',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Category.category'
        db.alter_column(u'app_category', 'category', self.gf('django.db.models.fields.CharField')(unique='true', max_length=100))

        # Changing field 'Tags.tag'
        db.alter_column(u'app_tags', 'tag', self.gf('django.db.models.fields.CharField')(unique='true', max_length=100))

    def backwards(self, orm):
        # Deleting field 'OpenCourse.rating'
        db.delete_column(u'app_opencourse', 'rating')

        # Deleting field 'OpenCourse.panelrating'
        db.delete_column(u'app_opencourse', 'panelrating')


        # Changing field 'Category.category'
        db.alter_column(u'app_category', 'category', self.gf('django.db.models.fields.CharField')(max_length=200, unique='true'))

        # Changing field 'Tags.tag'
        db.alter_column(u'app_tags', 'tag', self.gf('django.db.models.fields.CharField')(max_length=200, unique='true'))

    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'unique': "'true'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.opencourse': {
            'Meta': {'ordering': "['rating']", 'object_name': 'OpenCourse'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['app.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'panelrating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'pubDate': ('django.db.models.fields.DateField', [], {}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '5'}),
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