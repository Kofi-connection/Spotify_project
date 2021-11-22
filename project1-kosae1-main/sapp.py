import os 
import requests
import json
import random
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def get_song_info():
    AUTH_URL="https://accounts.spotify.com/api/token"
    CLIENT_ID=os.getenv("CLIENT_ID")
    CLIENT_SECRET=os.getenv("CLIENT_SECRET")
    auth_response =requests.post(AUTH_URL,{
      'grant_type':'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
    })

    

    auth_response_data=auth_response.json()

    access_token = auth_response_data['access_token']

    headers={
      'Authorization':'Bearer {token}'.format(token=access_token)
    }
    artist_id=["5f7VJjfbwm532GiveGC0ZK","1HY2Jd0NmPuamShAr6KMms","5YGY8feqx7naU7z4HrwZM6"]

    id = random.choice(artist_id)
    BASE_URL=f'https://api.spotify.com/v1/artists/{id}/top-tracks?market=US'

    r=requests.get(BASE_URL, headers=headers)
    r=r.json()
    #r_json=json.dumps(r, indent=4)
    #print(r_json)
    #any index from 0-9 will work

    
    artistname=r["tracks"][0]["artists"][0]["name"]
    #print(artistname)   
    
    track=r['tracks'][0]['name']
    #print(track)    
    
    preview_url=r['tracks'][0]['preview_url']
    #print(preview_url)    
    
        #find the proper path to it
    image=r['tracks'][0]['album']['images'][0]['url']
    

    obj=[artistname,track,preview_url,image]    
    
    
    
    
    
    return obj

get_song_info()