import pygame
from circleshape import *
from constants import *

# class defining the player.
class player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
    rotation = 0

    # in the player class; Code copied from boot.dev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        white = pygame.Color(255, 255, 255) 
        try:
            pygame.draw.polygon(screen, white, self.triangle(), 2)
        except ValueError:
            print("Not enough positions")
        except TypeError:
            print("points are not a sequence or do not contain pairs")
