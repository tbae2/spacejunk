from django.shortcuts import render
from django.conf import settings
import os
from .models import LaunchSite,CountryScore
import json as js
from django.http import HttpResponse

# Create your views here.

def importLaunchSite(request):
    ## function that can be called via url to import the launch_site data into the database ##
    file_path = os.path.join(settings.DATA_STORE,'launch_site_data.json')
    with open(file_path) as ls_data:
        data = js.load(ls_data)
        
        obj_result = []
        for site in data:
            site_result = {
                "launch_site": site["LAUNCH_SITE"],
                "created": False
            }
            obj, created = LaunchSite.objects.get_or_create(
                site_code = site["SITE_CODE"],
                launch_site = site["LAUNCH_SITE"]
            )
            site_result["created"] = created

            obj_result.append(site_result)
        return HttpResponse(obj_result)

def importCountryScore(request):
    ### function that can be called via url to import the country score file to db ###
    file_path = os.path.join(settings.DATA_STORE,'country_score.json')
    with open(file_path) as country_stats:
        data = js.load(country_stats)

        obj_result = []
        for country in data:
            country_stat = {
                "country": country["COUNTRY"],
                "record": None,
                "created": False
            }
        obj,created = CountryScore.objects.get_or_create(
            launch_country = country["COUNTRY"],
            spadoc_cd = country["SPADOC_CD"],
            orbital_tba = country["ORBITAL_TBA"],
            orbital_payload_count = country["ORBITAL_PAYLOAD_COUNT"],
            orbital_total_count = country["ORBITAL_TOTAL_COUNT"],
            decayed_total_count = country["DECAYED_TOTAL_COUNT"],
            country_total = country["COUNTRY_TOTAL"],
        )
        country_stat["record"] = obj
        country_stat["created"] = created
        obj_result.append(country_stat)
    return HttpResponse(obj_result)