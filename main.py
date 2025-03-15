import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """
    Main function that initializes and runs the Asteroids game.
    
    This function sets up the game window, creates game objects,
    and runs the main game loop which handles events, updates game state,
    detects collisions, and renders the game.
    """
    # Initialize pygame and create the game window
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0  # Delta time (time since last frame)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create sprite groups to organize game objects:
    # - updatable: All objects that need to be updated each frame
    # - drawable: All objects that need to be drawn each frame
    # - asteroids: All asteroid objects (for collision detection)
    # - shots: All shot objects (for collision detection)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(x=SCREEN_WIDTH / 2,
                    y=SCREEN_HEIGHT / 2,
                    radius=PLAYER_RADIUS,
                    PLAYER_RADIUS=PLAYER_RADIUS)
    
    asteroid_field = AsteroidField()
    
    # Initialize scoring and game progression variables
    score = 0
    lives = PLAYER_LIVES
    level = 1
    
    # Initialize font for UI elements
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    
    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game when window is closed
        
        # Update all game objects with the current delta time
        updatable.update(dt)
        
        # Collision detection
        for asteroid in asteroids:
            # Check for collisions between the player and asteroids
            if player.collides_with(asteroid):
                lives -= 1
                if lives <= 0:
                    # Game over when all lives are lost
                    print("Game over! Final score:", score)
                    return
                else:
                    # Reset player position after losing a life
                    # This gives the player a moment to recover before potentially
                    # colliding with another asteroid
                    player.position.x = SCREEN_WIDTH / 2
                    player.position.y = SCREEN_HEIGHT / 2
                    player.velocity = pygame.Vector2(0, 0)
                    break  # Stop checking other asteroids after a collision
                    
            # Check for collisions between shots and this asteroid
            for shot in shots:
                if shot.collides_with(asteroid):
                    # Calculate score based on asteroid size (smaller = more points)
                    score += SCORE_PER_ASTEROID.get(asteroid.radius, 0)
                    # Split the asteroid into smaller pieces
                    asteroid.split()
                    # Remove the shot that hit the asteroid
                    shot.kill()
                    break  # Stop checking other shots for this asteroid
                    
        # Level up logic - increase difficulty as score increases
        if score >= level * LEVEL_UP_SCORE:
            level += 1
            # Reset the spawn timer to immediately spawn a new asteroid
            # This effectively increases the spawn rate as the player levels up
            asteroid_field.spawn_timer = 0
            # Note: We can't modify ASTEROID_SPAWN_RATE directly as it's a constant,
            # but resetting the timer makes asteroids spawn more frequently
        
        # Rendering section
        # Clear the screen with black background
        pygame.Surface.fill(screen, color="black")
        
        # Draw all game objects (player, asteroids, shots)
        for sprite in drawable:
            sprite.draw(screen)
            
        # Draw UI elements in the top-left corner
        # Show current score
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        
        # Show remaining lives
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (10, 50))
        
        # Show current level
        level_text = font.render(f"Level: {level}", True, "white")
        screen.blit(level_text, (10, 90))
        
        # Update the display to show everything we've drawn
        pygame.display.flip()
        
        # Calculate delta time (time since last frame in seconds)
        # This ensures consistent game speed regardless of frame rate
        dt = clock.tick(60) / 1000  # Target 60 FPS
        


    
if __name__ == "__main__":
    main()