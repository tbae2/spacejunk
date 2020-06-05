from django.db import models

# Create your models here.


class LaunchSite(models.Model):
    site_code = models.CharField(max_length=10,default=None)
    launch_site = models.CharField(max_length=50,default=None)
    

class CountryScore(models.Model):
    launch_country = models.CharField(max_length=100,default=None)
    spadoc_cd = models.CharField(max_length=5,default=None)
    orbital_tba = models.IntegerField(default=None)
    orbital_payload_count = models.IntegerField(default=None)
    orbital_total_count = models.IntegerField(default=None)
    decayed_total_count = models.IntegerField(default=None)
    country_total = models.IntegerField(default=None)
    