import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Chase Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player class (the one the AI will chase)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# AI class (chasing the player)
class AI(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.target = target
        self.speed = 3

    def update(self):
        # Calculate direction to the player
        direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
        if direction.length() != 0:
            direction.normalize_ip()
        
        # Move towards the player
        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed

# Create the player and AI instances
player = Player()
ai = AI(player)

# Sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(ai)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the keys pressed
    keys = pygame.key.get_pressed()
    
    # Update game objects
    player.update(keys)
    ai.update()
    
    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()