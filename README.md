# Asteroids Game

A Python implementation of the classic Asteroids arcade game using Pygame.

## Description
This is a simple asteroid game created using the help of Boot.dev. The game features a player-controlled spaceship that can shoot and destroy asteroids while trying to survive.

## Features
- Ship movement with WASD controls
- Asteroid spawning and splitting mechanics
- Shooting with cooldown timing
- Scoring system based on asteroid size
- Lives system with 3 initial lives
- Level progression that increases difficulty
- UI showing score, lives, and current level

## Prerequisites
- Python 3.10+
- Pygame (see requirements.txt)

## Installation
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the game: `python main.py`

## How to Play
- Use **W** to thrust forward
- Use **A** and **D** to rotate left and right
- Use **S** to move backward
- Press **SPACE** to shoot
- Avoid colliding with asteroids
- Destroy asteroids to earn points:
  - Small asteroids: 100 points
  - Medium asteroids: 50 points
  - Large asteroids: 25 points

## Game Mechanics
- You start with 3 lives
- Shooting asteroids breaks them into 2 smaller asteroids unless they're already the smallest size
- Colliding with an asteroid costs you a life
- Reach score thresholds to level up, which increases the game difficulty
- Game ends when you lose all your lives

## Code Structure
- `main.py`: Game initialization and main loop
- `player.py`: Player ship class and controls
- `asteroid.py`: Asteroid behavior and splitting logic
- `shot.py`: Projectile mechanics
- `asteroidfield.py`: Handles spawning of new asteroids
- `circleshape.py`: Base class for game objects
- `constants.py`: Game configuration values

## Credits
Created with guidance from Boot.dev
