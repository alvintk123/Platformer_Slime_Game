from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from tilemap import TileMap

if TYPE_CHECKING:
    from main import Game

JUMPING_ACTIVE   = 1
JUMPING_INACTIVE = -1
from tilemap import TileMap
class PhysicsEntity:
    def __init__(self, game: Game, e_type: str, pos: tuple[int, int], size: tuple[int, int]) -> None:
        self.game = game
        self.type = e_type
        self.pos  = list(pos)
        self.size = size
        
        self.velocity = [0, 0]
        
        # Direction flag for character
        self.flip = False
        # set default action
        self.action = ''
        self.set_action('idle')
    
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        
    def set_action(self, action: str) -> None:
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + action].copy()
            
    def update(self, tileMap: TileMap, movement: tuple[int, int]=(0, 0)) -> None:
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frameMovement[0]
        entityRect = self.rect()
        for rect in tileMap.physicRectAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[0] > 0:
                    entityRect.right = rect.left
                    self.collisions['right'] = True
                if frameMovement[0] < 0:
                    entityRect.left =rect.right
                    self.collisions['left'] = True
                
                # update position of image 
                self.pos[0] = entityRect.x
        
        self.pos[1] += frameMovement[1] 
        entityRect = self.rect()
        for rect in tileMap.physicRectAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[1] > 0:
                    entityRect.bottom = rect.top
                    self.collisions['down'] = True
                if frameMovement[1] < 0:
                    entityRect.top =rect.bottom
                    self.collisions['up'] = True
                
                # update position of image
                self.pos[1] = entityRect.y
            
            
        # Update direction flag
        if movement[0] == 1:
            self.flip = False
        elif movement[0] == -1:
            self.flip = True
            
        # Add gravity force 
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        # Hold player don't out of screen
        if (self.pos[1] >= self.game.display.get_height() - (int(self.game.player.animation.img().get_height())+1)):
            self.pos[1] = self.game.display.get_height() - (int(self.game.player.animation.img().get_height())+1)
        # Update image for animation
        self.animation.update()
        
    def render(self, displaySurf, offset = (0, 0)):
        displaySurf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        pygame.draw.rect(displaySurf, (255, 255, 255), (self.pos[0] - offset[0], self.pos[1] - offset[1], *self.size), width=1)
        

class Player(PhysicsEntity): 
    def __init__(self, game: Game, pos: tuple[int, int], size: tuple[int, int]):
        super().__init__(game, 'player', pos, size)
        self.isJump = JUMPING_ACTIVE
    
    def jumping(self: Player):
        self.velocity[1] = -3
        
    def update(self: Player, movement=(0, 0)):
        super().update(movement)
    
    def render(self: Player, displaySurf, offset=(0, 0)):
        super().render(displaySurf, offset)
            