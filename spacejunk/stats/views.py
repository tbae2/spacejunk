from django.shortcuts import render
from django.conf import settings
import os
from .models import LaunchSite
import json as js
from django.http import HttpResponse

# Create your views here.

def importLaunchSite(request):
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
