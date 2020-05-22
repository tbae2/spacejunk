from skyfield.api import EarthSatellite,Topos,load
import json
import time


def processTle():

    with open("../datastore/tle_data.json") as tle_data:
        data = json.load(tle_data)
        ts = load.timescale()
        calc_time = ts.now()
        for tle in data:
            tle_line1 = tle["TLE_LINE1"]
            tle_line2 = tle["TLE_LINE2"]
            name = tle["OBJECT_NAME"]
            satellite = EarthSatellite(tle_line1,tle_line2,name,ts)
            geocentric = satellite.at(calc_time)
            subpoint = geocentric.subpoint()
            print('Latitude:', subpoint.latitude.degrees)
            print('Longitude:', subpoint.longitude.degrees)
            print(satellite)



