import sys
import pygame

from utils import load_images
from tilemap import TileMap

FPS = 60

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
        
        # save the key
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
            
            # get mouse position
            mpos = pygame.mouse.get_pos()
            # print(mpos)
            
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
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
        
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
            
Editor().run()