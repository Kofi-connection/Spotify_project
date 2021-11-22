##Prject 1 ReadMe
## Link to heroku https://quiet-reaches-70236.herokuapp.com
## Link to heroku for project milestone2  https://glacial-sands-01821.herokuapp.com


## Frameworks
Flask, Heroku, html, css, Git+github
 
## Technologies
.gitignore, .env
 
## libraries
    Flask==2.0.1
 
    requests==2.26.0
 
    lyricsgenius==3.0.1
 
    python-dotenv==0.19.0
## Seting up the Database
   pip install psycopg2-binary
   pip install Flask-SQLAlchemy==2.1
   The above sets up a postgresql with flask-sqlalchemy. 
   

## Unsolved Issues
   The forms still doesnt take the user from the user in a correct manner and this neeeds to be fixed. 
   I proposed a way to do this but it doesn't work properly. 
  
## APIs
Spotify,Genius
 
## How someone who forks the repository would be able to get set up on the project (installations, secret files).
This project uses Spotify API and Genius API, Therefore, we have to register on Spotify and Genius API websites and get the client ids and client secrets and API keys and store them in a .env file in the top level directory of this project.
    Then you will be able to run it on a terminal, run python3 app.py locally.
    or you can create a heroku account and deploy the project there by several commands.
 
#### about the .env file, it looks like this:
    export CLIENT_ID=“your id”
    export CLIENT_SECRET="yoursecret”
    export GENIUS_KEY=“your Genius API key”
 
 
#### heroku:  Deployment system to launch your app to the world.
You can also come up with a fun name related to your theme. Remember to follow instructions for things like installing the CLI, using the correct commands to login, create, and push, and adding the necessary setup files such as requirements.txt and Procfile. See Getting Started with Heroku on Python.

