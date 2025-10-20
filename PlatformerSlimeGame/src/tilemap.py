import pygame

class TileMap:
    def __init__(self, game, tile_size=16):
        self.game          = game
        self.tileSize      = tile_size
        
        # create a dictionary and list for store ttype, variant and pos for image
        self.tileMap       = {}
        self.offGridTtiles = []
        for i in range(10):
            self.tileMap[str(1 + i) + ';10'] = {'type': 'stone', 'variant': 1, 'pos': (1+i, 10)}
            self.tileMap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
        
    
    def render(self, displaySurf, offset = (0, 0)):
        
        
        # Render all tile in tile map
        for x in range(offset[0] // self.tileSize, (offset[0] + displaySurf.get_width())// self.tileSize + 1):
            for y in range(offset[1] // self.tileSize, (offset[1] + displaySurf.get_height())//self.tileSize + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tileMap:
                    tile = self.tileMap[loc]
                    displaySurf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0]*self.tileSize - offset[0], tile['pos'][1]*self.tileSize - offset[1]))