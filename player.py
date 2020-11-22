from settings import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.mouse_x = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_d]:
            self.x += -player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse(self):
        x = pygame.mouse.get_pos()[0]
        if self.mouse_x != x:
            xo = abs(self.mouse_x - x)
            if x > self.mouse_x:
                self.angle += 0.05
            elif x < self.mouse_x:
                self.angle -= 0.05
        
        self.mouse_x = x