import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Sprites Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Sprite class
class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create sprite group
all_sprites = pygame.sprite.Group()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add new sprite at mouse click position
            pos = pygame.mouse.get_pos()
            sprite = SimpleSprite(pos[0], pos[1])
            all_sprites.add(sprite)

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()