import pygame
import sys

FPS = 30
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Rimuru - Slime')
        
        self.screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
        self.display = pygame.Surface((320, 240))
        
        self.clock = pygame.time.Clock()
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print('Presss')
                        
            self.screen.blit(self.display, (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
    
# Run game
Game().run()