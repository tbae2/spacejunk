from pprint import pprint
from space_track_api import SpaceTrackApi
import configparser
import json



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
        start_id = norad_id_start
        end_id = norad_id_end
        norad_cat_id_range = f"{start_id}--{end_id}"

        with SpaceTrackApi(login=self.st_login,password=self.st_password) as stapi:
            tle_data = stapi.tle_latest(NORAD_CAT_ID=norad_cat_id_range)
            with open('../datastore/tle_data.json', 'w') as tle_file:
                tle_file.write(json.dumps(tle_data))
    
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