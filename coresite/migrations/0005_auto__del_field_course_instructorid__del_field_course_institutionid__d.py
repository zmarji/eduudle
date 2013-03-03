# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.execute("DROP SEQUENCE instructor_id_seq CASCADE")
        db.execute("CREATE SEQUENCE instructor_id_seq")
        db.execute("SELECT setval('instructor_id_seq', (SELECT MAX(id) FROM instructor))")
        db.execute("ALTER TABLE instructor ALTER COLUMN id SET DEFAULT nextval('instructor_id_seq'::regclass)")
        db.execute("ALTER SEQUENCE instructor_id_seq OWNED BY instructor.id")
        # Deleting field 'Course.instructorid'
        db.delete_column(u'course', 'instructorId')

        # Deleting field 'Course.institutionid'
        db.delete_column(u'course', 'institutionId')

        # Adding field 'Course.institution'
        db.add_column(u'course', 'institution',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['coresite.Institution'], db_column='institutionId'),
                      keep_default=False)

        # Adding field 'Course.instructor'
        db.add_column(u'course', 'instructor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['coresite.Instructor'], db_column='instructorId'),
                      keep_default=False)

        # Adding field 'Course.cost'
        db.add_column(u'course', 'cost',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Course.instructorid'
        db.add_column(u'course', 'instructorid',
                      self.gf('django.db.models.fields.IntegerField')(null=True, db_column='instructorId', blank=True),
                      keep_default=False)

        # Adding field 'Course.institutionid'
        db.add_column(u'course', 'institutionid',
                      self.gf('django.db.models.fields.IntegerField')(null=True, db_column='institutionId', blank=True),
                      keep_default=False)

        # Adding field 'Course.course'
        db.add_column(u'course', 'course',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Course.institution'
        db.delete_column(u'course', 'institutionId')

        # Deleting field 'Course.instructor'
        db.delete_column(u'course', 'instructorId')

        # Deleting field 'Course.cost'
        db.delete_column(u'course', 'cost')


    models = {
        'coresite.category': {
            'Meta': {'object_name': 'Category', 'db_table': "u'category'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'coresite.course': {
            'Meta': {'object_name': 'Course', 'db_table': "u'course'"},
            'categoryid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'categoryId'", 'blank': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'duration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infourl': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'infoUrl'", 'blank': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['coresite.Institution']", 'db_column': "'institutionId'"}),
            'instructor': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['coresite.Instructor']", 'db_column': "'instructorId'"}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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