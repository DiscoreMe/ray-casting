import pygame 
from pygame.constants import QUIT
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting

pygame.init()
pygame.mouse.set_visible(True)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()

DEBUG = False

font = pygame.font.SysFont("Arial", 36, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            player.mouse()

        player.movement()
        sc.fill(BLACK)

        if DEBUG:
            pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
            pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                                    player.y + WIDTH * math.sin(player.angle)))
            for x, y in world_map:
                pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)
        else:
            pygame.draw.rect(sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
            ray_casting(sc, player.pos, player.angle)

        render = font.render(str(int(clock.get_fps())), 0, RED)
        sc.blit(render, (WIDTH-65, 5))

        pygame.display.flip()
        clock.tick(FPS)
