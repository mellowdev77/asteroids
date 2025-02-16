import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    if pygame.get_init():
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.Surface.fill(screen, (255, 0, 0))

        while True:
            for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
            pygame.Surface.fill(screen, (255, 0, 0))
            pygame.display.flip()

if __name__ == "__main__":
    main()