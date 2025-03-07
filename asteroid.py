from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        if hasattr(self, 'containers'):
            self.add(*self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)

        child_rock_ang_1 = self.velocity.rotate(new_angle)
        child_rock_ang_2 = self.velocity.rotate(-new_angle)
        
        child_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, child_radius)
        asteroid.velocity = child_rock_ang_1 * 1.2

        asteroid = Asteroid(self.position.x, self.position.y, child_radius)
        asteroid.velocity = child_rock_ang_2 * 1.2


