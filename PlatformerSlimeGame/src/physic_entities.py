import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos  = list(pos)
        self.size = size
        
        self.velocity = [0, 0]
        
        # set default action
        self.action = ''
        self.set_action('idle')
    
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + action].copy()
            
    def update(self):
        
        # Update image for animation
        self.animation.update()
        
    def render(self, displaySurf):
        displaySurf.blit(self.animation.img(), self.pos)