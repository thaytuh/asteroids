from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # first split asteroid
            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid1.velocity = velocity1 * 1.2
            
            # second split asteroid
            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid2.velocity = velocity2 * 1.2