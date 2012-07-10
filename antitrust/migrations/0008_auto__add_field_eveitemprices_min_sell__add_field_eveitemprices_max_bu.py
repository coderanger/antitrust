# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EveItemPrices.min_sell'
        db.add_column('antitrust_eveitemprices', 'min_sell',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=7, decimal_places=2),
                      keep_default=False)

        # Adding field 'EveItemPrices.max_buy'
        db.add_column('antitrust_eveitemprices', 'max_buy',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=7, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EveItemPrices.min_sell'
        db.delete_column('antitrust_eveitemprices', 'min_sell')

        # Deleting field 'EveItemPrices.max_buy'
        db.delete_column('antitrust_eveitemprices', 'max_buy')


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
            'max_buy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'mean_all': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'mean_buy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'mean_sell': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'median_all': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'median_buy': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'median_sell': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'min_sell': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'region': ('django.db.models.fields.IntegerField', [], {})
        },
        'antitrust.eveneareststation': {
            'Meta': {'unique_together': "(('system_id', 'creation_hash'),)", 'object_name': 'EveNearestStation'},
            'creation_hash': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nearest_station': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nearest_system': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['antitrust']