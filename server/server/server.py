import json
import spotipy
"""
Create a 'secrets.py' file in the same directory with three lines containing:
username='YOUR_USERNAME'
client_id='CLIENT_ID'
client_secret='CLIENT_SECRET'"""
import secrets

# Authenticate Spotify.
USERNAME = secrets.username
CLIENT_ID = secrets.client_id
CLIENT_SECRET = secrets.client_secret
redirect_uri = 'http://localhost:7777/callback'
scope = "user-top-read"
oauth_object = spotipy.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri, scope=scope)
token_dict = oauth_object.get_cached_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)

top_tracks = spotify_object.current_user_top_tracks(time_range="short_term", limit=50)['items']
# List comprehension. For every JSON item in top_tracks, I only want the key value pair 'album'.
albums = [x['album'] for x in top_tracks]

top_albums_length = 0
album_counts = {}   # Key: album_id || Value: Frequency of album in user's top tracks.
album_img_urls = {} # Key: album_id || Value: URL of album cover.
for album in albums:
    if top_albums_length is 10: break
    album_id = album['id']
    if album_id not in album_counts:
        album_counts[album_id] = 1
        album_img_urls[album_id] = album['images'][0]['url']
    else:
        album_counts[album_id] += 1
    top_albums_length += 1