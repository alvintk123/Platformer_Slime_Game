import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}
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
    
    # Find tile map around position
    # return -> list of dictionary of tile (type, variant, pos)
    def tilesAround(self, pos):
        tiles = []
        tileLocation = (int(pos[0]//self.tileSize), int(pos[1]//self.tileSize))
        for offset in NEIGHBOR_OFFSETS:
            checkLoc = str(tileLocation[0] + offset[0]) + ";" + str(tileLocation[1] + offset[1])
            if checkLoc in self.tileMap:
                tiles.append(self.tileMap[checkLoc])
        return tiles
    
    # Check if having tiles around 
    # return lis of rect of tiles aro und
    def physicRectAround(self, pos):
        rects = []
        for tile in self.tilesAround(pos):
            if tile['type'] in PHYSICS_TILES:
                pos = tile['pos']
                rects.append(pygame.Rect(pos[0]*self.tileSize, pos[1]*self.tileSize, self.tileSize, self.tileSize))
        return rects
    
    def render(self, displaySurf, offset = (0, 0)):
        
        # Render all tile in tile map
        for x in range(offset[0] // self.tileSize, (offset[0] + displaySurf.get_width())// self.tileSize + 1):
            for y in range(offset[1] // self.tileSize, (offset[1] + displaySurf.get_height())//self.tileSize + 1):
                loc = str(x) + ';' + str(y)
                if loc in self.tileMap:
                    tile = self.tileMap[loc]
                    displaySurf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0]*self.tileSize - offset[0], tile['pos'][1]*self.tileSize - offset[1]))