from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import json as js
import datetime
from .models import tle_record,satellite
# Create your views here.

def index(request):
    """ main page to show the map and available options"""
    return HttpResponse("stubbed response place holder")
        




def importTle(request):

    file_path = os.path.join(settings.DATA_STORE,'proc_tle_load.json')

    with open(file_path,'r') as tle_data:
        data = js.load(tle_data)
        obj_result = []
        
        for tle in data:
            tle_stat = {
                "norad_cat_id": tle["NORAD_CAT_ID"],
                "object_name": tle["OBJECT_NAME"],
                "tle1": tle["TLE_LINE1"],
                "tle2": tle["TLE_LINE2"],
                "created": False
            }
            obj,created = tle_record.objects.get_or_create(
                norad_cat_id        = tle["NORAD_CAT_ID"],
                object_name         = tle["OBJECT_NAME"],
                object_type         = tle["OBJECT_TYPE"],
                object_id           = tle["OBJECT_ID"],
                classification_type = tle["CLASSIFICATION_TYPE"],
                intldes             = tle["INTLDES"],
                epoch               = tle["EPOCH"],
                epoch_microseconds  = tle["EPOCH_MICROSECONDS"],
                tle1                = tle["TLE_LINE1"],
                tle2                = tle["TLE_LINE2"],
                period              = tle["PERIOD"],
                apogee              = tle["APOGEE"],
                perigee             = tle["PERIGEE"],
                decayed             = tle["DECAYED"],
                latitude            = tle["Latitude"],
                longitude           = tle["Longitude"],
            )
            tle_stat["created"] = created
            obj_result.append(tle_stat)
        return HttpResponse(obj_result)


def importSatellites(request):
    file_path = file_path = os.path.join(settings.DATA_STORE,'satcat_data.json')


    with open(file_path,'r') as sat_data:
        obj_result = []
        data = js.load(sat_data)
        for sat in data:
            sat_stat = {
                "satname": sat["SATNAME"],
                "norad_cat_id": sat["NORAD_CAT_ID"],
                "site": sat["SITE"],
                "created": False
            }
            obj, created = satellite.objects.get_or_create(
                intldes      = sat["INTLDES"],
                object_name  = sat["SATNAME"],
                object_id    = sat["OBJECT_ID"],
                norad_cat_id = sat["NORAD_CAT_ID"],
                country      = sat["COUNTRY"],
                launch       = sat["LAUNCH"],
                launch_year  = sat["LAUNCH_YEAR"],
                site         = sat["SITE"],
            )
            sat_stat["created"] = created
            obj_result.append(sat_stat)
        return HttpResponse(obj_result)
