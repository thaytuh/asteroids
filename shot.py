from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt