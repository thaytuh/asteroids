from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    """
    Represents the player's ship in the game.
    
    The Player class handles movement, rotation, and shooting functionality.
    It inherits from CircleShape for collision detection.
    """
    def __init__(self, x, y, radius, PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.PLAYER_RADIUS = PLAYER_RADIUS
        self.rotation = 0
        self.shoot_timer = 0
    
    
        
    def triangle(self):
        """
        Calculates the three points that make up the player's triangular ship.
        
        Returns:
            list: Three points (pygame.Vector2) representing the triangle vertices.
        """
        # Get a unit vector pointing in the direction the ship is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Calculate a perpendicular vector (right) for the base of the triangle
        # Scale it to be smaller than the forward vector to create a proper triangle shape
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # Calculate the three points of the triangle:
        # a = front/nose of the ship
        # b = bottom-left corner
        # c = bottom-right corner
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        """
        Draws the player's ship as a triangle on the screen.
        
        Args:
            screen: The pygame surface to draw on.
        """
        pygame.draw.polygon(screen, "white",self.triangle(), width=2)
        
    def rotate(self, dt):
        """
        Rotates the player's ship clockwise.
        
        Args:
            dt: Delta time in seconds since last frame.
        """
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
        
    def update(self, dt):
        """
        Updates the player's state based on keyboard input.
        
        Handles rotation, movement, and shooting controls.
        
        Args:
            dt: Delta time in seconds since last frame.
        """
        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Handle rotation controls
        if keys[pygame.K_a]:  # A key - rotate counter-clockwise
            self.rotation = self.rotation - (PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:  # D key - rotate clockwise
            self.rotate(dt)
            
        # Handle movement controls
        if keys[pygame.K_w]:  # W key - move forward
            self.move(dt)
        if keys[pygame.K_s]:  # S key - move backward
            self.move(-dt)
            
        # Update the shooting cooldown timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            
        # Handle shooting - only if cooldown timer has expired
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            # Reset the cooldown timer to prevent rapid-fire shooting
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        
    def move(self, dt):
        """
        Moves the player's ship in the direction it's facing.
        
        Args:
            dt: Delta time in seconds since last frame.
            
        Note:
            Positive dt moves forward, negative dt moves backward.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self):
        """
        Creates a new Shot object in the direction the player is facing.
        
        The shot is created at the player's position and travels in the
        direction the ship is pointing at PLAYER_SHOOT_SPEED velocity.
        """
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = direction * PLAYER_SHOOT_SPEED