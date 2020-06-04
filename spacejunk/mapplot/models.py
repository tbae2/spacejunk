from django.db import models


# Create your models here.

class tle_record(models.Model):
    norad_cat_id = models.CharField(max_length=10)
    object_name = models.CharField(max_length=20)
    object_type = models.CharField(max_length=20)
    object_id = models.CharField(max_length=20)
    classification_type = models.CharField(max_length=3)
    intldes = models.CharField(max_length=10)
    epoch = models.DateTimeField("Date launched")
    epoch_microseconds = models.CharField(max_length=10)
    tle1 = models.CharField(max_length=100)
    tle2 = models.CharField(max_length=100)
    period = models.CharField(max_length=10)
    apogee = models.CharField(max_length=10)
    perigee = models.CharField(max_length=10)
    decayed = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)

class satellite(models.Model):
    intldes = models.CharField(max_length=50)
    object_name = models.CharField(max_length=50)
    object_id = models.CharField(max_length=50)
    norad_cat_id = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    launch = models.DateField()
    launch_year = models.CharField(max_length=50)
    site = models.CharField(max_length=50)