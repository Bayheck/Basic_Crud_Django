from django.db import models

# Create your models here.
class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.cname

    class Meta:
        managed = False
        db_table = 'country'


class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    id = models.ForeignKey('Diseasetype', models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseasetype'


class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicservant'


class Record(models.Model):
    email = models.OneToOneField(Publicservant, models.DO_NOTHING, db_column='email', primary_key=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    email = models.OneToOneField(Doctor, models.DO_NOTHING, db_column='email', primary_key=True)
    id = models.ForeignKey(Diseasetype, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('email', 'id'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
