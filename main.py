import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids =  pygame.sprite.Group()
shots =  pygame.sprite.Group()
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, drawables, updatables)
    pygame.init()

    if pygame.get_init():
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x, y)
        asteroid_field = AsteroidField()
        time = pygame.time.Clock()
        dt = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # draw
            pygame.Surface.fill(screen, "darkgreen")

            for drawable in drawables:
                drawable.draw(screen)
            for updatable in updatables:
                updatable.update(dt)

            for asteroid in asteroids:
                player_collision_flag = asteroid.check_collision(player)

                if player_collision_flag == True:
                    print("Game over!")
                    return

                for shot in shots:
                    bullet_collision_flag = asteroid.check_collision(shot)

                    if bullet_collision_flag == True:
                        asteroid.split()
                        shot.kill()

            #finish draw    
            pygame.display.flip()
            dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()