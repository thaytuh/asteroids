import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    """
    Controls the spawning of asteroids in the game.
    
    The AsteroidField regularly creates new asteroids at the edges of the screen
    with random velocities pointing toward the play area. It handles the timing
    and positioning of new asteroid spawns.
    """
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """
        Initialize the asteroid field.
        
        Sets up the spawn timer and connects to the sprite containers.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Spawns a new asteroid with the given parameters.
        
        Args:
            radius: The radius of the asteroid to spawn
            position: A Vector2 representing the spawn position
            velocity: A Vector2 representing the initial velocity
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """
        Updates the asteroid field, potentially spawning new asteroids.
        
        This method is called each frame and increments the spawn timer.
        When the timer exceeds ASTEROID_SPAWN_RATE, a new asteroid is
        spawned at a random edge of the screen with a random trajectory
        toward the center of the screen.
        
        Args:
            dt: Delta time in seconds since last frame.
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)