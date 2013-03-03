# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = u'category'
    
    def __unicode__(self):
        return self.name

class InstructorToInstitution(models.Model):
    id = models.IntegerField(primary_key=True)
    instructorid = models.IntegerField(null=True, db_column='instructorId', blank=True) # Field name made lowercase.
    institutionid = models.IntegerField(null=True, db_column='institutionId', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'instructor_to_institution'


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    institutionid = models.IntegerField(null=True, db_column='institutionId', blank=True) # Field name made lowercase.
    #cost = models.ForeignKey(Institution, null=True, db_column='cost', blank=True)
    instructorid = models.IntegerField(null=True, db_column='instructorId', blank=True) # Field name made lowercase.
    shortdesc = models.CharField(max_length=250, db_column='shortDesc', blank=True) # Field name made lowercase.
    longdesc = models.TextField(db_column='longDesc', blank=True) # Field name made lowercase.
    joinurl = models.CharField(max_length=250, db_column='joinUrl', blank=True) # Field name made lowercase.
    infourl = models.CharField(max_length=250, db_column='infoUrl', blank=True) # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True)
    startdate = models.DateField(null=True, db_column='startDate', blank=True) # Field name made lowercase.
    enddate = models.DateField(null=True, db_column='endDate', blank=True) # Field name made lowercase.
    duration = models.DateField(null=True, blank=True)
    categoryid = models.IntegerField(null=True, db_column='categoryId', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=50, db_column='slug', blank=True)
    tags = models.TextField(blank=True)
    course = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'course'
    
    def __unicode__(self):
        return self.name
    
class Institution(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    url = models.CharField(max_length=250, blank=True)
    blurb = models.TextField(blank=True)
    slug = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = u'institution'
    
    def __unicode__(self):
        return self.name

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, db_column='firstName', blank=True) # Field name made lowercase.
    lastname = models.CharField(max_length=50, db_column='lastName', blank=True) # Field name made lowercase.
    blurb = models.TextField(blank=True)
    slug = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = u'instructor'
    
    def __unicode__(self):
        return self.firstname

