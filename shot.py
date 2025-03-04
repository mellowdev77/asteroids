from circleshape import CircleShape
import pygame

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(surface = screen, 
                           center=self.position, 
                           radius=self.radius, 
                           width=2, 
                           color="yellow")

    def update(self, dt):
        self.position += self.velocity * dt 