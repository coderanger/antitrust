# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'EveItem.forge_price'
        db.delete_column('antitrust_eveitem', 'forge_price')


    def backwards(self, orm):
        # Adding field 'EveItem.forge_price'
        db.add_column('antitrust_eveitem', 'forge_price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=7, decimal_places=2),
                      keep_default=False)


    models = {
        'antitrust.eveitem': {
            'Meta': {'object_name': 'EveItem'},
            'corp_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'corp_optimal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eve_group_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eve_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'antitrust.eveitemprices': {
            'Meta': {'object_name': 'EveItemPrices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prices'", 'to': "orm['antitrust.EveItem']"}),
            'mean_all': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'mean_buy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'mean_sell': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'median_all': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'median_buy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'median_sell': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'region': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['antitrust']