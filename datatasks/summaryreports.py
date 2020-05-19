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
        with SpaceTrackApi(login=self.st_login,password=self.st_password) as stapi:
            country_score = stapi.boxscore()
            pprint(country_score, indent=2)
            with open('../datastore/country_score.json','w') as score_file:
                score_file.write(json.dumps(country_score))
    
    def tle_dump(self):
        pass

if __name__ == '__main__':
    main()