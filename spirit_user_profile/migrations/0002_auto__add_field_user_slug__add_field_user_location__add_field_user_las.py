# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.utils import timezone


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.slug'
        db.add_column('auth_user', 'slug',
                      self.gf('spirit.utils.models.AutoSlugField')(db_index=False, default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'User.location'
        db.add_column('auth_user', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'User.last_seen'
        db.add_column('auth_user', 'last_seen',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=timezone.now(), blank=True),
                      keep_default=False)

        # Adding field 'User.last_ip'
        db.add_column('auth_user', 'last_ip',
                      self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.timezone'
        db.add_column('auth_user', 'timezone',
                      self.gf('django.db.models.fields.CharField')(default='UTC', max_length=32),
                      keep_default=False)

        # Adding field 'User.is_administrator'
        db.add_column('auth_user', 'is_administrator',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'User.is_moderator'
        db.add_column('auth_user', 'is_moderator',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'User.topic_count'
        db.add_column('auth_user', 'topic_count',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'User.comment_count'
        db.add_column('auth_user', 'comment_count',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.slug'
        db.delete_column('auth_user', 'slug')

        # Deleting field 'User.location'
        db.delete_column('auth_user', 'location')

        # Deleting field 'User.last_seen'
        db.delete_column('auth_user', 'last_seen')

        # Deleting field 'User.last_ip'
        db.delete_column('auth_user', 'last_ip')

        # Deleting field 'User.timezone'
        db.delete_column('auth_user', 'timezone')

        # Deleting field 'User.is_administrator'
        db.delete_column('auth_user', 'is_administrator')

        # Deleting field 'User.is_moderator'
        db.delete_column('auth_user', 'is_moderator')

        # Deleting field 'User.topic_count'
        db.delete_column('auth_user', 'topic_count')

        # Deleting field 'User.comment_count'
        db.delete_column('auth_user', 'comment_count')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'spirit_user_profile.user': {
            'Meta': {'object_name': 'User', 'db_table': "'auth_user'"},
            'comment_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_administrator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_moderator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('spirit.utils.models.AutoSlugField', [], {'db_index': 'False', 'max_length': '50', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '32'}),
            'topic_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['spirit_user_profile']