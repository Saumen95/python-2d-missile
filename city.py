import pygame
from config import *

class City(object):
    def __init__(self, number, max_cities):
        self.position = (number * SCREENSIZE[0] // (max_cities + 1), SCREENSIZE[1] - GROUND_LEVEL)
        self.color = CITY
        self.size = 10
        self.destroyed = False


    def draw(self, screen):
        if self.destroyed != True:
            return pygame.draw.circle(screen, self.color, self.position, self.size)


    def update(self):
        pass


    def set_destroy(self, status):
        self.destroyed = status


    def get_destroy(self):
        return self.destroyed


    def get_position(self):
        return self.position
