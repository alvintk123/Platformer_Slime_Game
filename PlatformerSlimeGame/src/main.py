import pygame
import sys
from utils import load_image, load_images


FPS = 30
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rimuru - Slime')
        
        self.screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
        self.display = pygame.Surface((320, 240), pygame.SRCALPHA)
        
        self.clock = pygame.time.Clock()
        
        # --------------- load image --------------
        # Create assest dictionary for image
        self.assets = {
            # Background
            'background': load_image('ui/backgrounds/background.png'),
            'player/idle': load_images('sprites/player/run', 1),
        }

        self.count = 0
        

    def run(self):
        while True:
            self.display.fill((0, 0, 0, 0))
            
            # blit background 
            self.display.blit(self.assets['background'], (0, 0))
            
            # blit character
            self.display.blit(self.assets['player/idle'][self.count], (50, 50))
            self.count += 1
            if self.count >= len(self.assets['player/idle']):
                self.count = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print('Presss')
                        
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
    
# Run game
Game().run()