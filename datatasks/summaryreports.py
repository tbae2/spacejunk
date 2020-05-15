from pprint import pprint
from space_track_api import SpaceTrackApi
import configparser
import json



def main():
    pass
    config = configparser.ConfigParser()
    config.read('../configs/config.ini')
    spacetrack = config['spacetrack']
    st_login = spacetrack['login']
    st_password = spacetrack['password']
    with SpaceTrackApi(login=st_login, password=st_password) as stapi:
        country_score = stapi.boxscore()
        pprint(country_score, indent=2)
        with open('../datastore/country_score.json','w') as score_file:
            score_file.write(json.dumps(country_score))
    

if __name__ == '__main__':
    main()