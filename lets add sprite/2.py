import pygame
import random

# Requires: pip install pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60

class RandomSprite(pygame.sprite.Sprite):
    def __init__(self, color, radius, pos):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=pos)

        # use float position for smooth movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.velocity = pygame.math.Vector2(0, 0)
        self.max_speed = 200  # pixels per second
        self.change_timer = 0.0

    def update(self, dt):
        # occasionally change direction
        self.change_timer -= dt
        if self.change_timer <= 0:
            angle = random.uniform(0, 360)
            speed = random.uniform(self.max_speed * 0.2, self.max_speed)
            self.velocity = pygame.math.Vector2(speed, 0).rotate(angle)
            self.change_timer = random.uniform(0.3, 1.2)

        # move
        self.pos += self.velocity * dt
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        # keep inside window (bounce)
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.centerx
            self.velocity.x *= -1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.pos.x = self.rect.centerx
            self.velocity.x *= -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.pos.y = self.rect.centery
            self.velocity.y *= -1
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.pos.y = self.rect.centery
            self.velocity.y *= -1

# create two sprites
s1 = RandomSprite((255, 50, 50), 24, (200, 150))
s2 = RandomSprite((50, 150, 255), 32, (600, 450))
all_sprites = pygame.sprite.Group(s1, s2)

running = True
while running:
    dt = CLOCK.tick(FPS) / 1000.0  # seconds since last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    all_sprites.update(dt)

    SCREEN.fill((30, 30, 30))
    all_sprites.draw(SCREEN)
    pygame.display.flip()

pygame.quit()