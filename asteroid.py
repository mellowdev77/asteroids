from circleshape import CircleShape
import pygame 
from constants import *
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface = screen, 
                           center=self.position, 
                           radius=self.radius, 
                           width=2, 
                           color="white")

    def update(self, dt):
        self.position += self.velocity * dt 
    
    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        child_1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        child_1.velocity = self.velocity.rotate(angle)
        child_2 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        child_2.velocity = self.velocity.rotate(-angle)