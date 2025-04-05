import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    pygame.init()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    asteriods = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriods, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for asteriod in asteriods:
            if asteriod.collision_check(player):
                print("Game over!")
                exit()
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
