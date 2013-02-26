# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'category', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('coresite', ['Category'])

        # Adding model 'InstructorToInstitution'
        db.create_table(u'instructor_to_institution', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('instructorid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='instructorId', blank=True)),
            ('institutionid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='institutionId', blank=True)),
        ))
        db.send_create_signal('coresite', ['InstructorToInstitution'])

        # Adding model 'Course'
        db.create_table(u'course', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('institutionid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='institutionId', blank=True)),
            ('instructorid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='instructorId', blank=True)),
            ('shortdesc', self.gf('django.db.models.fields.CharField')(max_length=250, db_column='shortDesc', blank=True)),
            ('longdesc', self.gf('django.db.models.fields.TextField')(db_column='longDesc', blank=True)),
            ('joinurl', self.gf('django.db.models.fields.CharField')(max_length=250, db_column='joinUrl', blank=True)),
            ('infourl', self.gf('django.db.models.fields.CharField')(max_length=250, db_column='infoUrl', blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('startdate', self.gf('django.db.models.fields.DateField')(null=True, db_column='startDate', blank=True)),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, db_column='endDate', blank=True)),
            ('duration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('categoryid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='categoryId', blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='shortDesc', blank=True)),
            ('tags', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('course', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('coresite', ['Course'])

        # Adding model 'Institution'
        db.create_table(u'institution', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('blurb', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('coresite', ['Institution'])

        # Adding model 'Instructor'
        db.create_table(u'instructor', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='firstName', blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50, db_column='lastName', blank=True)),
            ('blurb', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('coresite', ['Instructor'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'category')

        # Deleting model 'InstructorToInstitution'
        db.delete_table(u'instructor_to_institution')

        # Deleting model 'Course'
        db.delete_table(u'course')

        # Deleting model 'Institution'
        db.delete_table(u'institution')

        # Deleting model 'Instructor'
        db.delete_table(u'instructor')


    models = {
        'coresite.category': {
            'Meta': {'object_name': 'Category', 'db_table': "u'category'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'coresite.course': {
            'Meta': {'object_name': 'Course', 'db_table': "u'course'"},
            'categoryid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'categoryId'", 'blank': 'True'}),
            'course': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'endDate'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'infourl': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'infoUrl'", 'blank': 'True'}),
            'institutionid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'institutionId'", 'blank': 'True'}),
            'instructorid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'instructorId'", 'blank': 'True'}),
            'joinurl': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'joinUrl'", 'blank': 'True'}),
            'longdesc': ('django.db.models.fields.TextField', [], {'db_column': "'longDesc'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'shortdesc': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_column': "'shortDesc'", 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'shortDesc'", 'blank': 'True'}),
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
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
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