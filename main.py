import pygame
from constants import *
from player import Player

def main(screen_width, screen_height):
    pygame.init()
    dt = 0
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
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        player.draw(screen)

        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


    

if __name__ == '__main__':
    main(SCREEN_WIDTH, SCREEN_HEIGHT)

