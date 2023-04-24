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
        self.top_albums = [track['album'] for track in self.top_tracks]
        """
        albums_info:
        list of dictionaries:
            { 
                'id': value,
                'frequency': value,
                'url': value
                'ranking': value
            }
        """
        self.albums_info = [] 
        self.set_albums_info()

    #run time complexity is not the most efficient 
    def set_albums_info(self):     
        albums_length = 0
        seen_ids = []
        for album in self.top_albums: 
            if albums_length == 10: break
            album_id = album['id']
            if album_id not in seen_ids:
                album_obj = {}
                album_obj['id'] = album_id
                album_obj['frequency'] = 1
                album_obj['url'] = album['images'][0]['url']
                album_obj['ranking'] = albums_length
                albums_length += 1
                self.albums_info.append(album_obj)
                seen_ids.append(album_id)
            else:
                for dic in self.albums_info:
                    if dic['id'] == album_id:
                        dic['frequency'] += 1

        return self.albums_info
    
if __name__ == "__main__":
    sp = Spotify()
    with open('dump4.json', 'w') as dump:
        dump.write(json.dumps(sp.albums_info, sort_keys=False))