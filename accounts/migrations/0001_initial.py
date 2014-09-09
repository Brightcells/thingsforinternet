# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserInfo'
        db.create_table(u'userinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sof', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weibo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rren', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('v2ex', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('blog', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('btc', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('freeze', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'accounts', ['UserInfo'])


    def backwards(self, orm):
        # Deleting model 'UserInfo'
        db.delete_table(u'userinfo')


    models = {
        u'accounts.userinfo': {
            'Meta': {'object_name': 'UserInfo', 'db_table': "u'userinfo'"},
            'blog': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'btc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'freeze': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rren': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'sof': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'v2ex': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weibo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']
