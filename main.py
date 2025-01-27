import pygame
from constants import *

def main(screen_width, screen_height):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print('Starting asteroids!')
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        # game goes here

        
        pygame.display.flip()

        clock.tick(60)


    

if __name__ == '__main__':
    main(SCREEN_WIDTH, SCREEN_HEIGHT)

