# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EveItem.pi_purchase'
        db.add_column('antitrust_eveitem', 'pi_purchase',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EveItem.pi_purchase'
        db.delete_column('antitrust_eveitem', 'pi_purchase')


    models = {
        'antitrust.eveitem': {
            'Meta': {'object_name': 'EveItem'},
            'corp_count': ('django.db.models.fields.IntegerField', [], {}),
            'eve_id': ('django.db.models.fields.IntegerField', [], {}),
            'forge_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pi_purchase': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['antitrust']