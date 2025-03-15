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
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
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
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                lives -= 1
                if lives <= 0:
                    print("Game over! Final score:", score)
                    return
                else:
                    # Reset player position after losing a life
                    player.position.x = SCREEN_WIDTH / 2
                    player.position.y = SCREEN_HEIGHT / 2
                    player.velocity = pygame.Vector2(0, 0)
                    break
                    
            for shot in shots:
                if shot.collides_with(asteroid):
                    # Calculate score based on asteroid size
                    score += SCORE_PER_ASTEROID.get(asteroid.radius, 0)
                    asteroid.split()
                    shot.kill()
                    break
                    
        # Level up logic
        if score >= level * LEVEL_UP_SCORE:
            level += 1
            # Increase difficulty by spawning asteroids faster
            asteroid_field.spawn_timer = 0
            # We can't modify ASTEROID_SPAWN_RATE directly as it's a constant,
            # but we could adjust the spawn timer in the asteroid field instance
        
        pygame.Surface.fill(screen, color="black")
        
        # Draw game objects
        for sprite in drawable:
            sprite.draw(screen)
            
        # Draw UI elements
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (10, 50))
        
        level_text = font.render(f"Level: {level}", True, "white")
        screen.blit(level_text, (10, 90))
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


    
if __name__ == "__main__":
    main()