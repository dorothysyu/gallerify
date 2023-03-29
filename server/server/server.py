import json
import spotipy
"""
Create a 'secrets.py' file in the same directory with three lines containing:
username='YOUR_USERNAME'
client_id='CLIENT_ID'
client_secret='CLIENT_SECRET'
"""
import secrets


class Spotify():
    # Authenticate Spotify.
    def __init__(self):
        USERNAME = secrets.username
        CLIENT_ID = secrets.client_id
        CLIENT_SECRET = secrets.client_secret
        redirect_uri = 'http://localhost:7777/callback'
        scope = "user-top-read"
        oauth_object = spotipy.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri, scope=scope)
        token_dict = oauth_object.get_cached_token()
        token = token_dict['access_token']
        self.spotify_object = spotipy.Spotify(auth=token)
    
        self.top_tracks = self.spotify_object.current_user_top_tracks(time_range="short_term", limit=50)['items']
        # List comprehension. For every JSON item in top_tracks, I only want the key value pair 'album'.
        self.albums = [x['album'] for x in self.top_tracks]
        """
        Key: album_id
        Value: List
            Index 0: integer representing frequency of album in user's top tracks.
            Index 1: string representing URL of album cover.
        """
        self.set_album_info()

    
    def set_album_info(self):
        self.album_info = {}        
        top_albums_length = 0
        for album in self.albums:
            if top_albums_length is 50: break
            album_id = album['id']
            if album_id not in self.album_info.keys():
                self.album_info[album_id] = [1]
                self.album_info[album_id].append(album['images'][0]['url'])
            else:
                self.album_info[album_id][0] += 1
            top_albums_length += 1
        return self.album_info
    
if __name__ == "__main__":
    sp = Spotify()
    print("running")
    with open('dump3.json', 'w') as dump:
        dump.write(json.dumps(sp.album_info, sort_keys=False))