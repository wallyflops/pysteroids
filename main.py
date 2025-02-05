import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
# from circleshape import CircleShape


def main(screen_width, screen_height):
    pygame.init()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print('Starting asteroids!')
    print(f"Screen width: {screen_width}")
    print(f"Screen height: {screen_height}")
    
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    # shot = Shot()
    
    # asteroid = Asteroid()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        # game goes here

        for thing in updateable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)
        
        for asteroid in asteroids:
            asteroid.check_collision(player)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


    

if __name__ == '__main__':
    main(SCREEN_WIDTH, SCREEN_HEIGHT)

