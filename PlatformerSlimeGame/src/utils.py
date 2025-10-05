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

class Animation:
    def __init__(self, images, imgDuration = 5, loopImg = True):
        self.imagesList  = images
        self.lenImgList  = len(self.imagesList)
        self.imgDuration = imgDuration
        self.loopImg     = loopImg
        self.frame       = 0
        self.done        = False
        
    def update(self):
        
        if self.loopImg:
            self.frame = (self.frame + 1)%(self.lenImgList*self.imgDuration)
            print(self.frame)
        else:
            self.frame = min(self.frame +1, self.lenImgList*self.imgDuration - 1)
            if (self.frame >= self.lenImgList*self.imgDuration - 1):
                self.done = True
                
    def copy(self):
        return Animation(self.imagesList, self.imgDuration, self.loopImg)
    
    def img(self):
        print(int(self.frame/self.imgDuration))
        return self.imagesList[int(self.frame/self.imgDuration)]