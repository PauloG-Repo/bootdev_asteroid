import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    clock = pygame.time.Clock()
    dt = 0

    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill('black')
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        log_state()
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
