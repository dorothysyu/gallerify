import json
import spotipy
"""
Set a SPOTIPY_CLIENT_ID environment variable. This can be done in the virtual env.
https://stackoverflow.com/a/38645983/9809952
"""
import os


class Spotify():
    # Authenticate Spotify.
    def __init__(self):
        oauth_object = spotipy.oauth2.SpotifyPKCE(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                                  redirect_uri='http://localhost:7777/callback',
                                                  scope="user-top-read")
        self.spotify_object = spotipy.Spotify(auth=oauth_object.get_access_token())
        self.top_tracks = self.spotify_object.current_user_top_tracks(time_range="short_term", limit=50)['items']
        # List comprehension. For every JSON item in top_tracks, I only want the key value pair 'album'.
        self.top_albums = [x['album'] for x in self.top_tracks]
        """
        albums_info attribute:
        Key: album_id
        Value: List
            Index 0: integer representing frequency of album in user's top tracks.
            Index 1: string representing URL of album cover.
        """
        self.albums_info = {}   
        self.set_albums_info()

    def set_albums_info(self):     
        top_albums_length = 0
        for album in self.top_albums:
            if top_albums_length is 50: break
            album_id = album['id']
            if album_id not in self.albums_info.keys():
                self.albums_info[album_id] = [1]
                self.albums_info[album_id].append(album['images'][0]['url'])
            else:
                self.albums_info[album_id][0] += 1
            top_albums_length += 1
        return self.albums_info
    
if __name__ == "__main__":
    sp = Spotify()
    with open('dump3.json', 'w') as dump:
        dump.write(json.dumps(sp.albums_info, sort_keys=False))