from settings import *

text_map = [
    'WWWWWWWWWWWW',
    'W.....WWWWWW',
    'W..........W',
    'W.........WW',
    'W..WWW.....W',
    'W..........W',
    'WWWWWWWWWWWW',
]

world_map =set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))