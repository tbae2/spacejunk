from skyfield.api import EarthSatellite,Topos,load
import json


def processTle():

    with open("../datastore/tle_data.json") as tle_data:
        data = json.load(tle_data)
        ts = load.timescale()
        for tle in data:
            tle_line1 = tle["TLE_LINE1"]
            tle_line2 = tle["TLE_LINE2"]
            name = tle["OBJECT_NAME"]
            satellite = EarthSatellite(tle_line1,tle_line2,name,ts)
            print(satellite)
            print(len(data))    
            print(tle["NORAD_CAT_ID"])
            print(tle["ORDINAL"])


