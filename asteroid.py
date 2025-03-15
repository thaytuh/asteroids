from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    """
    Represents an asteroid in the game.
    
    Asteroids move in straight lines and can split into smaller
    asteroids when hit by player shots. Asteroids inherit from
    CircleShape for movement and collision detection.
    """
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        """
        Draws the asteroid on the screen as a white circle.
        
        Args:
            screen: The pygame surface to draw on.
        """
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
        
    def update(self, dt):
        """
        Updates the asteroid's position based on its velocity.
        
        Args:
            dt: Delta time in seconds since last frame.
        """
        self.position += self.velocity * dt
        
    def split(self):
        """
        Removes this asteroid and creates two smaller ones if possible.
        
        If this asteroid is already at the minimum size (ASTEROID_MIN_RADIUS),
        it will simply be removed. Otherwise, it creates two smaller asteroids
        with slightly different trajectories and increased speeds.
        
        Returns:
            None
        """
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