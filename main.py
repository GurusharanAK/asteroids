import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    score = 0
    pygame.init()
    print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    asteriods = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriods, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()  # May look unused but it creates the asteroids

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
                print("------------------Game over!------------------")
                print("You has crashed on an asteriod...")
                print("You have destroyed", score, "asteroids!")
                print("Better luck next time!!!")
                print("----------------------------------------------")
                exit()
            for shot in shots:
                if asteriod.collision_check(shot):
                    shot.kill()
                    asteriod.split()
                    score += 1
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()
