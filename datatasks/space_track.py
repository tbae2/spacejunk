from pprint import pprint
from space_track_api import SpaceTrackApi
import configparser
import json
import math


def main():
    pass    
   
class space_track():

    def __init__(self):
        self.st_config = configparser.ConfigParser()
        self.st_config.read('../configs/config.ini')
        self.st_config = self.st_config['spacetrack']
        self.st_login = self.st_config['login']
        self.st_password = self.st_config['password']
    
    def dailyScore(self):
        # method that pulls the box score of countries and their number of satellites
        with SpaceTrackApi(login=self.st_login,password=self.st_password) as stapi:
            country_score = stapi.boxscore()
            pprint(country_score, indent=2)
            with open('../datastore/country_score.json','w') as score_file:
                score_file.write(json.dumps(country_score)) 
    
    def tle_dump(self,norad_id_end=0,norad_id_start=0):
        # method that pulls the most recent tle data for current satellites 
        # dependent on key args supplied or found within satcat_data 
        start_id = norad_id_start
        end_id = [norad_id_end]

        #determine start and end norard cat id's if only defaults provided (0,0)
        if start_id == 0 and end_id[0] == 0:
            with open("../datastore/satcat_data.json") as satcatfile:
                sat_data = json.load(satcatfile)
                norad_ids = []
                for sat in sat_data:
                    norad_ids.append(sat["NORAD_CAT_ID"])
                print(len(norad_ids))
                end_id.clear()
                end_id.append(len(norad_ids) + 1)
        
        with SpaceTrackApi(login=self.st_login,password=self.st_password) as stapi:
            print(end_id)
            if end_id[0] > 20000:
                end_id.insert(0, math.floor(end_id[0]/2))
            # combined output of 2 differnt spacetrack calls
            tle_combined = []
            # parse and produce startid and list of end norad cat ids 
            for endid in end_id:
                startid = start_id 
                if end_id.index(endid) > 0:
                    startid = end_id[end_id.index(endid) - 1]
                norad_cat_id_range = f"{startid}--{endid}"
                print(norad_cat_id_range)
                tle_combined  += stapi.tle_latest(NORAD_CAT_ID=norad_cat_id_range)
            with open('../datastore/tle_data.json', 'w') as tle_file:
                tle_file.write(json.dumps(tle_combined))
    
    def sat_cat(self):
        # method that will dump current sattelite catalog information
        with SpaceTrackApi(login=self.st_login,password=self.st_password) as stapi:
            satcat_data = stapi.satcat(CURRENT='Y')
            with open('../datastore/satcat_data.json', 'w') as satcat_file:
                satcat_file.write(json.dumps(satcat_data))

    def launch_sites(self):
        # method to dump list of satellite launch locations
        with SpaceTrackApi(login=self.st_login,password=self.st_password) as stapi:
            launch_sites = stapi.launch_site()
            with open('../datastore/launch_site_data.json','w') as launch_site_file:
                launch_site_file.write(json.dumps(launch_sites))
    
if __name__ == '__main__':
    main()