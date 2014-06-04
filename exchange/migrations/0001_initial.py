# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tips'
        db.create_table(u'tips', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tips', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('visit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('evaluate', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('like', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unlike', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('follow', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'exchange', ['Tips'])

        # Adding model 'UserTips'
        db.create_table(u'usertips', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('tips', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exchange.Tips'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'exchange', ['UserTips'])


    def backwards(self, orm):
        # Deleting model 'Tips'
        db.delete_table(u'tips')

        # Deleting model 'UserTips'
        db.delete_table(u'usertips')


    models = {
        u'accounts.userinfo': {
            'Meta': {'object_name': 'UserInfo', 'db_table': "u'userinfo'"},
            'blog': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'btc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
        },
        u'exchange.tips': {
            'Meta': {'object_name': 'Tips', 'db_table': "u'tips'"},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'evaluate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'follow': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tips': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'unlike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'exchange.usertips': {
            'Meta': {'object_name': 'UserTips', 'db_table': "u'usertips'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tips': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exchange.Tips']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['exchange']