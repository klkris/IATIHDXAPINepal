from django.db import models
from unittest.util import _MAX_LENGTH

    
class HXLData(models.Model):
    
    district = models.CharField(max_length=50)
    population = peopleInjured = models.IntegerField(default=0)    
    peopleInjured = models.IntegerField(default=0)
    femalesInjured = models.IntegerField(default=0)
    malesInjured = models.IntegerField(default=0)    
    peopleDead = models.IntegerField(default=0)
    femalesDead = models.IntegerField(default=0)
    malesDead = models.IntegerField(default=0)    
    housesDamaged = models.IntegerField(default=0)
    housesDestroyed = models.IntegerField(default=0)


    def __str__(self):
        return self.district
    
class IATIData(models.Model):
    
    iatiId = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    reportingOrg = models.CharField(max_length=2000)
    telephone = models.CharField(max_length=2000, default='')
    email = models.CharField(max_length=2000, default='')
    website = models.CharField(max_length=2000, default='')


    def __str__(self):
        return self.iatiId
    
class ShelterData(models.Model):
    
    district = models.CharField(max_length=50)
    blankets = models.IntegerField(default=0)
    cgi = models.IntegerField(default=0)
    clothes = models.IntegerField(default=0) 
    kitchenSets = models.IntegerField(default=0) 
    tarpaulin = models.IntegerField(default=0)    
    tents = models.IntegerField(default=0)


    def __str__(self):
        return self.district
    
   
     






    