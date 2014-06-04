# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NavInfo'
        db.create_table(u'navinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('func', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dh.FunctionInfo'], null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['NavInfo'])

        # Adding model 'ClassifyInfo'
        db.create_table(u'classifyinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('visit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('nav', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resources.NavInfo'], null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['ClassifyInfo'])

        # Adding model 'WebSiteInfo'
        db.create_table(u'websiteinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('srcode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('visit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('evaluate', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('like', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('unlike', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fav', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['WebSiteInfo'])

        # Adding model 'WebsiteRelatedInfo'
        db.create_table(u'websiterelatedinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='related_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('srcode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['WebsiteRelatedInfo'])

        # Adding model 'TagInfo'
        db.create_table(u'taginfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='taginfo_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['TagInfo'])

        # Adding model 'CsySite'
        db.create_table(u'csysite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classify', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resources.ClassifyInfo'], null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='csysite_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['CsySite'])

        # Adding model 'Evaluate'
        db.create_table(u'evaluate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('host', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='evaluate_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['Evaluate'])

        # Adding model 'Like'
        db.create_table(u'like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('host', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='like_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('flag', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['Like'])

        # Adding model 'Favorite'
        db.create_table(u'favorite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('host', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='favorite_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['Favorite'])

        # Adding model 'Visit'
        db.create_table(u'visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('host', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='visit_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['Visit'])

        # Adding model 'Log'
        db.create_table(u'log', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('host', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='log_website', null=True, to=orm['resources.WebSiteInfo'])),
            ('descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['Log'])

        # Adding model 'WebSiteSubmit'
        db.create_table(u'websitesubmit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('deal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'resources', ['WebSiteSubmit'])

        # Adding model 'ApiInfo'
        db.create_table(u'apiinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('api', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('func', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
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
        db.send_create_signal(u'resources', ['ApiInfo'])

        # Adding model 'UserApiInfo'
        db.create_table(u'userapiinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('api', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['resources.ApiInfo'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.UserInfo'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'resources', ['UserApiInfo'])


    def backwards(self, orm):
        # Deleting model 'NavInfo'
        db.delete_table(u'navinfo')

        # Deleting model 'ClassifyInfo'
        db.delete_table(u'classifyinfo')

        # Deleting model 'WebSiteInfo'
        db.delete_table(u'websiteinfo')

        # Deleting model 'WebsiteRelatedInfo'
        db.delete_table(u'websiterelatedinfo')

        # Deleting model 'TagInfo'
        db.delete_table(u'taginfo')

        # Deleting model 'CsySite'
        db.delete_table(u'csysite')

        # Deleting model 'Evaluate'
        db.delete_table(u'evaluate')

        # Deleting model 'Like'
        db.delete_table(u'like')

        # Deleting model 'Favorite'
        db.delete_table(u'favorite')

        # Deleting model 'Visit'
        db.delete_table(u'visit')

        # Deleting model 'Log'
        db.delete_table(u'log')

        # Deleting model 'WebSiteSubmit'
        db.delete_table(u'websitesubmit')

        # Deleting model 'ApiInfo'
        db.delete_table(u'apiinfo')

        # Deleting model 'UserApiInfo'
        db.delete_table(u'userapiinfo')


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
        u'dh.appinfo': {
            'Meta': {'object_name': 'AppInfo', 'db_table': "u'appinfo'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'dh.functioninfo': {
            'Meta': {'object_name': 'FunctionInfo', 'db_table': "u'functioninfo'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dh.AppInfo']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'resources.apiinfo': {
            'Meta': {'object_name': 'ApiInfo', 'db_table': "u'apiinfo'"},
            'api': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'evaluate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'follow': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'func': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'unlike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'resources.classifyinfo': {
            'Meta': {'object_name': 'ClassifyInfo', 'db_table': "u'classifyinfo'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nav': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resources.NavInfo']", 'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'resources.csysite': {
            'Meta': {'object_name': 'CsySite', 'db_table': "u'csysite'"},
            'classify': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resources.ClassifyInfo']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'csysite_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.evaluate': {
            'Meta': {'object_name': 'Evaluate', 'db_table': "u'evaluate'"},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'evaluate_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.favorite': {
            'Meta': {'object_name': 'Favorite', 'db_table': "u'favorite'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'favorite_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.like': {
            'Meta': {'object_name': 'Like', 'db_table': "u'like'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'host': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'like_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.log': {
            'Meta': {'object_name': 'Log', 'db_table': "u'log'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'log_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.navinfo': {
            'Meta': {'object_name': 'NavInfo', 'db_table': "u'navinfo'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'func': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dh.FunctionInfo']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'resources.taginfo': {
            'Meta': {'object_name': 'TagInfo', 'db_table': "u'taginfo'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'taginfo_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.userapiinfo': {
            'Meta': {'object_name': 'UserApiInfo', 'db_table': "u'userapiinfo'"},
            'api': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['resources.ApiInfo']", 'null': 'True', 'blank': 'True'}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'})
        },
        u'resources.visit': {
            'Meta': {'object_name': 'Visit', 'db_table': "u'visit'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.UserInfo']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'visit_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.websiteinfo': {
            'Meta': {'object_name': 'WebSiteInfo', 'db_table': "u'websiteinfo'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'evaluate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fav': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'srcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'unlike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'resources.websiterelatedinfo': {
            'Meta': {'object_name': 'WebsiteRelatedInfo', 'db_table': "u'websiterelatedinfo'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'srcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'related_website'", 'null': 'True', 'to': u"orm['resources.WebSiteInfo']"})
        },
        u'resources.websitesubmit': {
            'Meta': {'object_name': 'WebSiteSubmit', 'db_table': "u'websitesubmit'"},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['resources']