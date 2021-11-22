import requests
import os
import json
from dotenv import find_dotenv, load_dotenv

import sapp

load_dotenv(find_dotenv())

#artist_name=sapp.get_song_info()[0]
#song_title=sapp.get_song_info()[1]

def get_lyrics(artist_name,song_title):
    base_url = 'https://api.genius.com'
    token=os.getenv('GENIUS_TOKEN')
    headers = {'Authorization': 'Bearer ' + token}
    search_url = base_url + '/search'
    data = {'q': artist_name + ' ' + song_title}
    response = requests.get(search_url, data=data, headers=headers)
    #genius_search_url = f"http://api.genius.com/search?q=%7Bsearch%7D&access_token=%7Bclient_access_token%7D"
    #data=requests.get(genius_search_url)
    response=response.json()
    r_json=json.dumps(response, indent=4)
    #print(r_json)
    songurl=response['response']['hits'][0]['result']['url']
    print(r_json)
    return response

get_lyrics('adonai','sarkodie')

    
 






#request_song_info(artist_name,song_title)