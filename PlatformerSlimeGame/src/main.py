import pygame
import sys
from utils import load_image, load_images, Animation
from physic_entities import PhysicsEntity, Player

FPS = 60
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
            'player/idle': Animation(load_images('sprites/player/idle', 1), imgDuration=5, loopImg=True),
            'player/run': Animation(load_images('sprites/player/run', 1), imgDuration=5, loopImg=True),
            'player/roll': Animation(load_images('sprites/player/roll', 1), imgDuration=5, loopImg=True),
            'player/hit': Animation(load_images('sprites/player/hit', 1), imgDuration=5, loopImg=True),
            'player/death': Animation(load_images('sprites/player/death', 1), imgDuration=5, loopImg=True),
        }
        
        # ----------------- movement -------------------
        self.movement = [False, False]
        self.scroll   = [0, 0]
        self.player = Player(self, pos=(0, 0), size=(13, 19))
        

    def run(self):
        while True:
            self.display.fill((0, 0, 0, 0))
            # blit background 
            self.display.blit(self.assets['background'], (0, 0))
            
            # offset for screen
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width()/2 - self.scroll[0])/30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height()/2 - self.scroll[1])/30  
            renderScroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            # Update img for character
            self.player.update((self.movement[1] - self.movement[0], 0))
            # Render player image
            self.player.render(self.display, offset=renderScroll)            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.jumping()
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
    
# Run game
Game().run()