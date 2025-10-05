import pygame
import os

IMG_PATH = '../assets/'

def load_image(path, scale = 1):
    img = pygame.image.load(IMG_PATH + path).convert()
    img = pygame.transform.scale(img, (img.get_width()/scale, img.get_height()/scale))
    
    # set background (black) -> transparent
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path, scale = 1):
    images = []
    listDirImage = sorted(os.listdir(IMG_PATH + path))
    for imgFileName in listDirImage:
        images.append(load_image(path+"/"+imgFileName))
    
    return images