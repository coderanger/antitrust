# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EveItem.corp_optimal'
        db.add_column('antitrust_eveitem', 'corp_optimal',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EveItem.corp_optimal'
        db.delete_column('antitrust_eveitem', 'corp_optimal')


    models = {
        'antitrust.eveitem': {
            'Meta': {'object_name': 'EveItem'},
            'corp_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'corp_optimal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eve_group_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eve_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'forge_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['antitrust']