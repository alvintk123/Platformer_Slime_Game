import pygame
import os

IMG_PATH = '../assets/'

def load_image(path, scale = 1):
    img = pygame.image.load(IMG_PATH + path).convert()
    img = pygame.transform.scale(img, (img.get_width()/scale, img.get_height()/scale))
    
    return img

