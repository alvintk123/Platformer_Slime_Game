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
            
    def update(self, movement=(0, 0)):
        
        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frameMovement[0]
        
        self.pos[1] += frameMovement[1]
        
        # Add gravity force 
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        # Hold player don't out of screen
        if (self.pos[1] >= self.game.display.get_height() - (int(self.game.player.animation.img().get_height())+1)):
            self.pos[1] = self.game.display.get_height() - (int(self.game.player.animation.img().get_height())+1)
        # Update image for animation
        self.animation.update()
        
    def render(self, displaySurf):
        displaySurf.blit(self.animation.img(), self.pos)