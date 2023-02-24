import json
import spotipy
import secrets

USERNAME = secrets.username
CLIENT_ID = secrets.clientId
CLIENT_SECRET = secrets.clientSecret
redirect_uri = 'http://localhost:7777/callback'

# getting information
scope = "user-top-read"
oauth_object = spotipy.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri, scope=scope)
token_dict = oauth_object.get_cached_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)

user = spotify_object.current_user()
top_tracks = spotify_object.current_user_top_tracks(time_range="short_term")['items']
# list comprehension python. for every json item, i only want the key value pair  'album'
albums = [x['album'] for x in top_tracks]
album_ids = [x['album']['id'] for x in top_tracks]
album_img_urls = [ x['album']['images'][0]['url'] for x in top_tracks]

with open('dump.json', 'w') as dump:
    dump.write(json.dumps(albums, sort_keys=False))