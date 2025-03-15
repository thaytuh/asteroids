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
        # Remove this asteroid from all sprite groups
        self.kill()
        
        # If the asteroid is already at minimum size, don't create new ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Calculate a random angle between 20-50 degrees for the split
            random_angle = random.uniform(20, 50)
            
            # Create two new velocity vectors by rotating the original velocity
            # in opposite directions by the random angle
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            
            # Calculate the new radius for child asteroids
            # Each split reduces the radius by ASTEROID_MIN_RADIUS
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # Create the first child asteroid at the same position
            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            # Make it slightly faster (1.2x) than the parent and assign its direction
            asteroid1.velocity = velocity1 * 1.2
            
            # Create the second child asteroid at the same position
            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            # Make it slightly faster (1.2x) than the parent and assign its direction
            asteroid2.velocity = velocity2 * 1.2