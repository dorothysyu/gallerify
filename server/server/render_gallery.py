from server.server import Spotify  # import statement for manage.py
# from server import Spotify  # import statement for server.py
from math import sin, cos
import pygame
from pygame import Surface
from pygame.sprite import Group, Sprite
import json
import wget
import os
import random
import glob

# Overriding the collision method to add padding in the collision detection.

# https://stackoverflow.com/a/31035335/9809952


def collide(sprite1, sprite2):
    # FOUR CASES
    padding = 5
    if (sprite1.rect.x + sprite1.rect.width + padding >= sprite2.rect.x and  # sprite1 right edge past sprite2 left edge
        # sprite1 left edge past sprite2 right edge
        sprite1.rect.x <= sprite2.rect.x + sprite2.rect.width + padding and
        sprite1.rect.y + sprite1.rect.height + padding >= sprite2.rect.y and
            sprite1.rect.y <= sprite2.rect.y + sprite2.rect.height + padding):
        return True
    return False


class Gallery(Group):

    def __init__(self, albums_info):
        self.albums_info = albums_info
        self.group = Group()

        self.background = Surface((2053, 3480), flags=0)
        self.background.fill(color=(99, 12, 0))

    # Generates position tuple along an archimedean spiral.
    def position_iterator(self, reverse):
        DEFAULT_STEP = 0.2  # radians
        STEP_SIZE = 10  # relative to base step size of each spiral function
        RADIUS = 10
        ECCENTRICITY = 1.7
        t = 0
        r = -1 if reverse else 1
        while True:  # indefinitely generates the "next" position
            t += DEFAULT_STEP * STEP_SIZE * r
            yield (((RADIUS * t * cos(t))/100 + 700), ((ECCENTRICITY * RADIUS * t * sin(t))/100 + 1300))

    def _assign_positions(self):
        percent_shrink = 1
        for album in self.albums_info:
            curArt = AlbumArt(album['id'], album['url'], percent_shrink)
            curFrame = Frame(percent_shrink)
            self._assign_position(album_art=curArt, frame=curFrame)
            album['xy'] = (curArt.rect.x, curArt.rect.y)  # for debugging
            percent_shrink -= .03
            print(curArt.rect)  # for debugging
            print("\t" + album['name'])

    def _assign_position(self, album_art, frame):
        position_iterator = self.position_iterator(True)
        frame = frame
        album_art.rect.x, album_art.rect.y = next(position_iterator)
        frame.rect.x, frame.rect.y = album_art.rect.x, album_art.rect.y
        while (pygame.sprite.spritecollideany(frame, self.group, collide)):
            album_art.rect.x, album_art.rect.y = next(position_iterator)
            frame.rect.x, frame.rect.y = album_art.rect.x, album_art.rect.y
        self.group.add(album_art)
        self.group.add(frame)

    def draw_group(self):
        self._assign_positions()
        self.group.draw(self.background)
        pygame.image.save(self.background, "images/test_img2.jpg")


class AlbumArt(Sprite):

    def __init__(self, album_id, image_url, percent_shrink):
        Sprite.__init__(self)
        self.album_id = album_id
        self.image_url = image_url
        self.percent_shrink = percent_shrink
        self._load_image()
        self.rect = self.image.get_rect()

    def _load_image(self):
        img_path = format("images/" + self.album_id+'.jpg')  # for manage.py
        if not os.path.exists(img_path):
            wget.download(self.image_url, out=img_path)
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(
            self.image, (640 * self.percent_shrink, 640 * self.percent_shrink))


class Frame(Sprite):
    def __init__(self, percent_shrink):
        Sprite.__init__(self)
        self.percent_shrink = percent_shrink
        self._load_image()
        self.rect = self.image.get_rect()

    def _load_image(self):
        frames = glob.glob("images/frames/*.png")
        frame = pygame.image.load(random.choice(frames))
        # frame = pygame.transform.smoothscale(frame, (640, 640))
        self.image = frame
        self.image = pygame.transform.scale(
            self.image, (670 * self.percent_shrink, 670 * self.percent_shrink))


if __name__ == "__main__":
    gallery = Gallery(albums_info=Spotify().albums_info)
    gallery.draw_group()
    with open('dump.json', 'w') as dump:
        dump.write(json.dumps(gallery.albums_info, sort_keys=False))
