# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OpenCourse.category'
        db.add_column(u'app_opencourse', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['app.Category']),
                      keep_default=False)

        # Adding M2M table for field tags on 'OpenCourse'
        m2m_table_name = db.shorten_name(u'app_opencourse_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('opencourse', models.ForeignKey(orm[u'app.opencourse'], null=False)),
            ('tags', models.ForeignKey(orm[u'app.tags'], null=False))
        ))
        db.create_unique(m2m_table_name, ['opencourse_id', 'tags_id'])


    def backwards(self, orm):
        # Deleting field 'OpenCourse.category'
        db.delete_column(u'app_opencourse', 'category_id')

        # Removing M2M table for field tags on 'OpenCourse'
        db.delete_table(db.shorten_name(u'app_opencourse_tags'))


    models = {
        u'app.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'unique': "'true'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.opencourse': {
            'Meta': {'object_name': 'OpenCourse'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['app.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'pubDate': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Tags']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.tags': {
            'Meta': {'object_name': 'Tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': "'true'", 'max_length': '200'})
        }
    }

    complete_apps = ['app']