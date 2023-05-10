from server.server import Spotify # import statement for manage.py
# from server import Spotify #import statement for server.py
from math import sin, cos
import pygame
from pygame import Surface
from pygame.sprite import Group, Sprite
import json
import wget
import os

class Gallery(Group):
    
    def __init__(self, albums_info):
        self.albums_info = albums_info
        self.group = Group()
        self.STEP_SIZE = 200 # relative to base step size of each spiral function
        self.RADIUS = 10
        self.ECCENTRICITY = 2
        
        self.background = Surface((2053, 3480), flags=0)
        self.background.fill(color=(161,0,14))

    # Generates position tuple using archimedean spiral.
    def position_iterator(self, reverse):
        DEFAULT_STEP = 0.5 # radians
        t = 0
        r = 1
        if reverse:
            r = -1
        while True: #indefinitely generates the "next" position
            t += DEFAULT_STEP * self.STEP_SIZE * r
            yield (((self.RADIUS * t * cos(t))/100) + 672, ((self.ECCENTRICITY * self.RADIUS * t * sin(t))/100) + 1480)
                
    def _assign_positions(self):
        for album in self.albums_info:
            curArt = AlbumArt(album['id'], album['url'])
            self._assign_position(album_art=curArt)
            album['xy'] = (curArt.rect.x, curArt.rect.y) # for debugging
            print(curArt.rect) # for debugging
        
    def _assign_position(self, album_art):
        position_iterator = self.position_iterator(False)
        album_art.rect.x, album_art.rect.y = next(position_iterator)
        while(pygame.sprite.spritecollideany(album_art, self.group)):
            album_art.rect.x, album_art.rect.y = next(position_iterator)
        self.group.add(album_art)
        
    # def collided(self, sprite1, sprite2):
    #     return pygame.sprite.collide_mask(sprite1, sprite2)
    
    def draw_group(self):
        self._assign_positions()
        self.group.draw(self.background)
        pygame.image.save(self.background, "images/test_img2.jpg")

class AlbumArt(Sprite):
    
    
    def __init__(self, album_id, image_url,):
        Sprite.__init__(self)
        self.album_id = album_id
        self.image_url = image_url
        self._load_image()
        self.rect = self.image.get_rect()
        
    def _load_image(self):
        img_path = format("images/" + self.album_id+'.jpg') #for manage.py
        if not os.path.exists(img_path):
            wget.download(self.image_url, out=img_path)
        self.image = pygame.image.load(img_path)
    
    
if __name__ == "__main__":
    gallery = Gallery(albums_info=Spotify().albums_info)
    gallery.draw_group()
    with open('dump.json', 'w') as dump:
        dump.write(json.dumps(gallery.albums_info, sort_keys=False))