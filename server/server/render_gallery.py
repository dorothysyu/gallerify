from server.server import Spotify # import statement for manage.py
# from server import Spotify #import statement for server.py
from math import sin, cos
import pygame
from pygame import Surface
from pygame.sprite import Group, Sprite
import json
import wget
import os

class Gallery():
    
    def __init__(self, albums_info):
        self.albums_info = albums_info
        self.img = Surface((1200, 1800), flags=0)
        self.img.fill(color=(161,0,14))
        self.STEP_SIZE = 200 # relative to base step size of each spiral function
        self.RADIUS = 5
        self.ECCENTRICITY = 3

    def _archimedean_spiral(self, reverse):
        DEFAULT_STEP = 0.05 # radians
        t = 0
        r = 1
        if reverse:
            r = -1
        while True: #indefinitely generates the "next" position
            t += DEFAULT_STEP * self.STEP_SIZE * r
            yield (self.RADIUS * t * cos(t), self.ECCENTRICITY * self.RADIUS * t * sin(t))
            

    """
    Takes in a dictionary:
        key: album_id
        value: list
            index 0: integer representing ranking of album in user's listening history
            index 1: integer representing how many times it shows up in user's listening
            index 3: string representing album cover url
    Returns spiral guy
    """
    def draw(self):
        xy_list = self._archimedean_spiral(False)
        for dic in self.albums_info:
            dic['xy'] = next(xy_list)
        
        self._test_download_imgs()
        pygame.image.save(self.img, "images/test_img.jpg") # for manage.py
        # pygame.image.save(self.img, "../images/test_img.jpg") # for server.py
        return 
    
    def _test_download_imgs(self):
        for album in self.albums_info:
            alb_cov = AlbumCover(album['id'], album['url'], album['xy'])
            img = pygame.image.load(format("images/" + album['id']+'.jpg'))
            self.img.blit(img, album['xy'])

class AlbumCover(Sprite):
    
    
    def __init__(self, album_id, image_url, xy):
        Sprite.__init__(self)
        if not os.path.exists(format("images/" + album_id+'.jpg')):
            wget.download(image_url, out=format("images/" + album_id+'.jpg'))
        
        
if __name__ == "__main__":
    gallery = Gallery(albums_info=Spotify().albums_info)
    gallery._test_download_imgs()
    with open('dump4.json', 'w') as dump:
        dump.write(json.dumps(gallery.albums_info, sort_keys=False))