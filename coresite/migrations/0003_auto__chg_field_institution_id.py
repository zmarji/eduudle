# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Institution.id'
        db.alter_column(u'institution', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'Institution.id'
        db.alter_column(u'institution', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        'coresite.category': {
            'Meta': {'object_name': 'Category', 'db_table': "u'category'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'coresite.course': {
            'Meta': {'object_name': 'Course', 'db_table': "u'course'"},
            'categoryid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'categoryId'", 'blank': 'True'}),
            'course': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infourl': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'infoUrl'", 'blank': 'True'}),
            'institutionid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'institutionId'", 'blank': 'True'}),
            'instructorid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'instructorId'", 'blank': 'True'}),
            'joinurl': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'joinUrl'", 'blank': 'True'}),
            'longdesc': ('django.db.models.fields.TextField', [], {'db_column': "'longDesc'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shortdesc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'shortDesc'", 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'slug'", 'blank': 'True'}),
            'startdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'startDate'", 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'coresite.institution': {
            'Meta': {'object_name': 'Institution', 'db_table': "u'institution'"},
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'coresite.instructor': {
            'Meta': {'object_name': 'Instructor', 'db_table': "u'instructor'"},
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'firstName'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'lastName'", 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'coresite.instructortoinstitution': {
            'Meta': {'object_name': 'InstructorToInstitution', 'db_table': "u'instructor_to_institution'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'institutionid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'institutionId'", 'blank': 'True'}),
            'instructorid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'instructorId'", 'blank': 'True'})
        }
    }

    complete_apps = ['coresite']