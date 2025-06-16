import pygame
import random
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carol of the Bells: Horror Santa")

clock = pygame.time.Clock()
font = pygame.font.SysFont('chiller', 50)

# Colors
RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load resources
santa_img = pygame.image.load("santa.jpg")

santa_img = pygame.transform.scale(santa_img, (80, 80))

# Music
pygame.mixer.music.load("carol_of_the_bells_horror.ogg")  # your horror remix
pygame.mixer.music.play(-1)

# Player
player = pygame.Rect(WIDTH//2, HEIGHT - 50, 40, 40)

# Enemies (Santas)
santas = []

def spawn_santa():
    x = random.randint(0, WIDTH - 80)
    rect = pygame.Rect(x, -80, 80, 80)
    santas.append(rect)

# Game Loop
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1000)

running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_event:
            spawn_santa()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5

    # Move and draw Santas
    for santa in santas[:]:
        santa.y += 4
        screen.blit(santa_img, (santa.x, santa.y))
        if santa.colliderect(player):
            text = font.render("Santa Got You!", True, RED)
            screen.blit(text, (WIDTH//3, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

    pygame.draw.rect(screen, WHITE, player)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()