from skyfield.api import EarthSatellite,Topos,load
import json
import time


def processTle():
    calculated_lat_long_tle = []
    with open("../datastore/tle_data.json") as tle_data:
        data = json.load(tle_data)
        ts = load.timescale()
        calc_time = ts.now()
        for tle in data:
            temp_tle = tle
            tle_line1 = temp_tle["TLE_LINE1"]
            tle_line2 = temp_tle["TLE_LINE2"]
            name = temp_tle["OBJECT_NAME"]
            satellite = EarthSatellite(tle_line1,tle_line2,name,ts)
            geocentric = satellite.at(calc_time)
            subpoint = geocentric.subpoint()
            # print('Latitude:', subpoint.latitude.degrees)
            # print('Longitude:', subpoint.longitude.degrees)
            # print(satellite)
            temp_tle["Latitude"] = subpoint.latitude.degrees
            temp_tle["Longitude"] = subpoint.longitude.degrees
            # print(temp_tle)
            calculated_lat_long_tle.append(temp_tle)
        with open("../datastore/proc_tle_load.json",'w') as proc_tle:
            proc_tle.write(json.dumps(calculated_lat_long_tle))


    



