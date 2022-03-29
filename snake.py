# Snake tutorial using Py Game
# Notes: tutorial itself doesn't seem to tell you much about Pygame in the beginning
# to import pygame, run the following: "pip install pygame==2.1.3 dev4" - basically grab the latest version....

import math
import random
import pygame
import tkinter as tk

pygame.init()

class cube(object):
    rows = 0
    w = 0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def _init_(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows # window divided by number of rows ??

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w)) # y coordinate does not change here; hence the 0. This is setup for x
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y)) # same as above but for y (x coord does not change...)
    pass

def redrawWindow(surface):
    global width, height, rows 
    surface.fill((0,0,0)) #this means the window is black lol (surface definition. some bullshit??)
    drawGrid(width, height, rows, surface)
    pygame.display.update()
    pass

def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

# FYI... this is the main loop
def main():
    global width, height, rows
    width = 500
    height = 500 #he took that variable out and uses width twice, but you are not going to do that because you want to make the window different as a challenge
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255,0,0), (10,10))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) # used for speed of the game to make it somewhat playable
        clock.tick(10) # used for speed of the game as well
        redrawWindow(win)




    pass

# __init__

