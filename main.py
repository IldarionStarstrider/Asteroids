#importing pygame:
import pygame
from constants import *

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        Clock.tick(60)
        dt = (Clock.tick(60) / 1000)
        pygame.display.flip()



if __name__ == "__main__":
    main()