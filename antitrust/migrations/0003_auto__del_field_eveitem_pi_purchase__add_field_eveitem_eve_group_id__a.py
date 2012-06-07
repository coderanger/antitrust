# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'EveItem.pi_purchase'
        db.delete_column('antitrust_eveitem', 'pi_purchase')

        # Adding field 'EveItem.eve_group_id'
        db.add_column('antitrust_eveitem', 'eve_group_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding unique constraint on 'EveItem', fields ['eve_id']
        db.create_unique('antitrust_eveitem', ['eve_id'])

        # Adding unique constraint on 'EveItem', fields ['name']
        db.create_unique('antitrust_eveitem', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'EveItem', fields ['name']
        db.delete_unique('antitrust_eveitem', ['name'])

        # Removing unique constraint on 'EveItem', fields ['eve_id']
        db.delete_unique('antitrust_eveitem', ['eve_id'])

        # Adding field 'EveItem.pi_purchase'
        db.add_column('antitrust_eveitem', 'pi_purchase',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'EveItem.eve_group_id'
        db.delete_column('antitrust_eveitem', 'eve_group_id')


    models = {
        'antitrust.eveitem': {
            'Meta': {'object_name': 'EveItem'},
            'corp_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eve_group_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'eve_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'forge_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '7', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['antitrust']