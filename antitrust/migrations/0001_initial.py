# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EveItem'
        db.create_table('antitrust_eveitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('eve_id', self.gf('django.db.models.fields.IntegerField')()),
            ('forge_price', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=2)),
            ('corp_count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('antitrust', ['EveItem'])


    def backwards(self, orm):
        # Deleting model 'EveItem'
        db.delete_table('antitrust_eveitem')


    models = {
        'antitrust.eveitem': {
            'Meta': {'object_name': 'EveItem'},
            'corp_count': ('django.db.models.fields.IntegerField', [], {}),
            'eve_id': ('django.db.models.fields.IntegerField', [], {}),
            'forge_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['antitrust']