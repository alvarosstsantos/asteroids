import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(color=(0, 0, 0))

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if (player.collide(a)):
                print("Game over!")
                sys.exit()

            for s in shots:
                if (a.collide(s)):
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
