from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    """
    Represents a projectile fired by the player.
    
    Shots travel in straight lines and can destroy asteroids.
    They inherit from CircleShape for movement and collision detection.
    """
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS
        
    def draw(self, screen):
        """
        Draws the shot on the screen as a solid white circle.
        
        Args:
            screen: The pygame surface to draw on.
        """
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
        
    def update(self, dt):
        """
        Updates the shot's position based on its velocity.
        
        Args:
            dt: Delta time in seconds since last frame.
        """
        self.position += self.velocity * dt