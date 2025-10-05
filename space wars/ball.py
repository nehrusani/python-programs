import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball settings
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 3  # Speed in x and y directions

# Clock to control FPS
clock = pygame.time.Clock()

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Move the ball
	ball_x += ball_dx
	ball_y += ball_dy

	# Bounce on walls
	if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
		ball_dx = -ball_dx
	if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
		ball_dy = -ball_dy

	# Drawing
	screen.fill(WHITE)
	pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
	pygame.display.flip()

	# FPS
	clock.tick(60)