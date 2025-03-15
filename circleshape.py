import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    Base class for circular game objects.
    
    Provides common functionality for positioning, movement,
    and collision detection for circular objects in the game.
    All game entities (Player, Asteroid, Shot) inherit from this class.
    """
    def __init__(self, x, y, radius):
        """
        Initialize a circular shape with position and radius.
        
        Args:
            x: X-coordinate of the shape's center
            y: Y-coordinate of the shape's center
            radius: Radius of the circular shape
        """
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """
        Draw the shape on the screen.
        
        Args:
            screen: The pygame surface to draw on.
            
        Note:
            This is an abstract method that subclasses must override.
        """
        pass

    def update(self, dt):
        """
        Update the shape's state for the current frame.
        
        Args:
            dt: Delta time in seconds since last frame.
            
        Note:
            This is an abstract method that subclasses must override.
        """
        pass
    
    def collides_with(self, other):
        """
        Check if this shape collides with another circular shape.
        
        Uses simple distance-based collision detection between circles.
        
        Args:
            other: Another CircleShape object to check collision with.
            
        Returns:
            bool: True if the shapes are colliding, False otherwise.
        """
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)