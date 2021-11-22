import os

from flask import Flask, render_template
import sapp
from genius import get_lyrics
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

artistname=sapp.get_song_info()[0]
songtitle=sapp.get_song_info()[1]


@app.route('/')
def spot():
    #Genius stuff

    lyrics=get_lyrics(artistname,songtitle)
    return render_template(
        "index.html",
        artist_name=artistname,
        song_name=songtitle,
        preview_url=sapp.get_song_info()[2],
        image=sapp.get_song_info()[3],
        song_lyrics=lyrics
    )
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
