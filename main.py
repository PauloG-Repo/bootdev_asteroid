import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot



def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()
    dt = 0

    Shot.containers = (shots, drawable, updatable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill('black')
        updatable.update(dt)
        for obj in asteroids:
            if obj.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()
            for shot in shots:
                if obj.collides_with(shot):
                    log_event('asteroid_shot')
                    obj.split()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)
        log_state()
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
