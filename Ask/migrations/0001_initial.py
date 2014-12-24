# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Turma'
        db.create_table(u'matbasica_turma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('semestre', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'matbasica', ['Turma'])

        # Adding model 'Usuario'
        db.create_table(u'matbasica_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_usuario', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('tipo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('senha', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('turma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Turma'], null=True, blank=True)),
        ))
        db.send_create_signal(u'matbasica', ['Usuario'])

        # Adding model 'Conteudo'
        db.create_table(u'matbasica_conteudo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tema', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pergunta_inicial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Pergunta'], null=True, blank=True)),
            ('linha_metro', self.gf('django.db.models.fields.IntegerField')()),
            ('tamanho_metro', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'matbasica', ['Conteudo'])

        # Adding model 'Pergunta'
        db.create_table(u'matbasica_pergunta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('item_correto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Item'], null=True, blank=True)),
            ('conteudo_pertence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Conteudo'])),
        ))
        db.send_create_signal(u'matbasica', ['Pergunta'])

        # Adding model 'Ajuda'
        db.create_table(u'matbasica_ajuda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('conteudo_pertence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Conteudo'], null=True, blank=True)),
        ))
        db.send_create_signal(u'matbasica', ['Ajuda'])

        # Adding model 'Item'
        db.create_table(u'matbasica_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('pergunta_pertence', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pertence', to=orm['matbasica.Pergunta'])),
            ('tipo_proximo', self.gf('django.db.models.fields.IntegerField')(default=True)),
            ('pergunta_proximo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='proximo', null=True, to=orm['matbasica.Pergunta'])),
            ('conteudo_proximo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Conteudo'], null=True, blank=True)),
            ('ajuda_proximo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Ajuda'], null=True, blank=True)),
        ))
        db.send_create_signal(u'matbasica', ['Item'])

        # Adding model 'Busca_Ajuda'
        db.create_table(u'matbasica_busca_ajuda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Usuario'])),
            ('pergunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Pergunta'])),
            ('ajuda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Ajuda'])),
        ))
        db.send_create_signal(u'matbasica', ['Busca_Ajuda'])

        # Adding model 'Historico'
        db.create_table(u'matbasica_historico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Usuario'])),
            ('turma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Turma'])),
            ('conteudo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Conteudo'])),
            ('pergunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Pergunta'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Item'])),
            ('data', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('acertou', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'matbasica', ['Historico'])

        # Adding model 'Estado_Usuario'
        db.create_table(u'matbasica_estado_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('turma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Turma'])),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Usuario'])),
            ('conteudo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Conteudo'])),
            ('pergunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matbasica.Pergunta'])),
        ))
        db.send_create_signal(u'matbasica', ['Estado_Usuario'])


    def backwards(self, orm):
        # Deleting model 'Turma'
        db.delete_table(u'matbasica_turma')

        # Deleting model 'Usuario'
        db.delete_table(u'matbasica_usuario')

        # Deleting model 'Conteudo'
        db.delete_table(u'matbasica_conteudo')

        # Deleting model 'Pergunta'
        db.delete_table(u'matbasica_pergunta')

        # Deleting model 'Ajuda'
        db.delete_table(u'matbasica_ajuda')

        # Deleting model 'Item'
        db.delete_table(u'matbasica_item')

        # Deleting model 'Busca_Ajuda'
        db.delete_table(u'matbasica_busca_ajuda')

        # Deleting model 'Historico'
        db.delete_table(u'matbasica_historico')

        # Deleting model 'Estado_Usuario'
        db.delete_table(u'matbasica_estado_usuario')


    models = {
        u'matbasica.ajuda': {
            'Meta': {'ordering': "['descricao']", 'object_name': 'Ajuda'},
            'conteudo_pertence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Conteudo']", 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'matbasica.busca_ajuda': {
            'Meta': {'ordering': "['usuario']", 'object_name': 'Busca_Ajuda'},
            'ajuda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Ajuda']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pergunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Pergunta']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Usuario']"})
        },
        u'matbasica.conteudo': {
            'Meta': {'ordering': "['tema']", 'object_name': 'Conteudo'},
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linha_metro': ('django.db.models.fields.IntegerField', [], {}),
            'pergunta_inicial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Pergunta']", 'null': 'True', 'blank': 'True'}),
            'tamanho_metro': ('django.db.models.fields.IntegerField', [], {}),
            'tema': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'matbasica.estado_usuario': {
            'Meta': {'ordering': "['usuario']", 'object_name': 'Estado_Usuario'},
            'conteudo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Conteudo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pergunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Pergunta']"}),
            'turma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Turma']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Usuario']"})
        },
        u'matbasica.historico': {
            'Meta': {'ordering': "['data']", 'object_name': 'Historico'},
            'acertou': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'conteudo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Conteudo']"}),
            'data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Item']"}),
            'pergunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Pergunta']"}),
            'turma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Turma']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Usuario']"})
        },
        u'matbasica.item': {
            'Meta': {'ordering': "['descricao']", 'object_name': 'Item'},
            'ajuda_proximo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Ajuda']", 'null': 'True', 'blank': 'True'}),
            'conteudo_proximo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Conteudo']", 'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pergunta_pertence': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pertence'", 'to': u"orm['matbasica.Pergunta']"}),
            'pergunta_proximo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'proximo'", 'null': 'True', 'to': u"orm['matbasica.Pergunta']"}),
            'tipo_proximo': ('django.db.models.fields.IntegerField', [], {'default': 'True'})
        },
        u'matbasica.pergunta': {
            'Meta': {'ordering': "['descricao']", 'object_name': 'Pergunta'},
            'conteudo_pertence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Conteudo']"}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_correto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Item']", 'null': 'True', 'blank': 'True'})
        },
        u'matbasica.turma': {
            'Meta': {'ordering': "['semestre']", 'object_name': 'Turma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'semestre': ('django.db.models.fields.FloatField', [], {})
        },
        u'matbasica.usuario': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Usuario'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nome_usuario': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'senha': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tipo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'turma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matbasica.Turma']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['matbasica']