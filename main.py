import pygame
import sys
from pygame.mixer_music import play
from asteroid import Asteroid # type: ignore
from asteroidfield import AsteroidField # type: ignore
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot # type: ignore

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    asteroids = pygame.sprite.Group()
    
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable) # type: ignore
    Asteroid.containers = (asteroids,updatable, drawable) # type: ignore
    AsteroidField.containers = updatable # type: ignore
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for sprite in updatable:
            sprite.update(dt)


        for asteroid in asteroids:
            if player.handle_colision(asteroid):
                print('Game Over')
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.handle_colision(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill(000)

        for sprite in drawable:
            sprite.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
