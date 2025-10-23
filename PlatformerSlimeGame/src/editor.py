import sys
import pygame

from utils import load_images
from tilemap import TileMap

FPS = 60
RENDER_SCALE = 2
class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Editor')
        
        self.screen  = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))
        self.clock   = pygame.time.Clock()
        
        
        self.assets = {
            'large_decor': load_images('sprites/environment/tiles/large_decor'),
            'stone': load_images('sprites/environment/tiles/stone'),
        }
        
        self.movement = [False, False, False, False]
        
        self.tileMap  = TileMap(self, tile_size=16)
        
        self.scroll = [0, 0]
        
        # save the list key of dictionary
        self.tileList = list(self.assets) 
        self.tileGroup = 0
        self.tileVariant = 0
        
        self.clicking = False
        self.rightClicking = False
        self.shift = False
        self.onGrid = True
        
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
            
            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2
            
            renderScroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.tileMap.render(self.display, offset=renderScroll)
            
            # Get current tile image
            curTileImg = self.assets[self.tileList[self.tileGroup]][self.tileVariant].copy()
            # get mouse position
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0]//RENDER_SCALE, mpos[1]//RENDER_SCALE)
            # print(mpos)
            imgPos = (int((mpos[0]+renderScroll[0])//self.tileMap.tileSize), int((mpos[1]+renderScroll[1])//self.tileMap.tileSize))
            if self.clicking:
                self.tileMap.tileMap[str(imgPos[0])+';'+str(imgPos[1])] = {'type': self.tileList[self.tileGroup], 'variant': self.tileVariant, 'pos': imgPos}
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        print(self.clicking)
                    if event.button == 3:
                        self.rightClicking = True
                        print(self.rightClicking)
                    if self.shift:
                        if event.button == 4:
                            self.tileVariant = (self.tileVariant - 1) % len(self.assets[self.tileList[self.tileGroup]])
                        if event.button == 5:
                            self.tileVariant = (self.tileVariant + 1) % len(self.assets[self.tileList[self.tileGroup]])
                    else:
                        if event.button == 4:
                            self.tileGroup = (self.tileGroup - 1) % len(self.tileList)
                            self.tileVariant = 0
                        if event.button == 5:
                            self.tileGroup = (self.tileGroup + 1) % len(self.tileList)
                            self.tileVariant = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.rightClicking = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False
                        
            self.display.blit(curTileImg, (int(imgPos[0]*self.tileMap.tileSize-renderScroll[0]), int(imgPos[1]*self.tileMap.tileSize-renderScroll[1])))
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
            
Editor().run()