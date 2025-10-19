import pygame 
import random

SCREEN_WIDTH , SCREEN_HEIGHT = 500 , 400
MOVMENT_SPEED = 5
FONT_SIZE = 72

pygame.init

background_image = pygame.transform.scale(pygame.image.load("space.jpeg"),(SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x = max(min(self.rect.x + x_change,SCREEN_WIDTH - self.rect.width),0)
        self.rect.y = max(min(self.rect.y + y_change,SCREEN_HEIGHT- self.rect.height),0)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("sprite collision")
all_sprites = pygame.sprite.Group()

Sprite_1 = Sprite(pygame.color('black'),20,30)
Sprite_1.rect.x,Sprite_1.rect.y = random.randint(0,SCREEN_WIDTH - Sprite_1.rect.width),random.randint(0,SCREEN_HEIGHT-Sprite_1.rect.height)
all_sprites.add(Sprite_1)

Sprite_2 = Sprite(pygame.color('red'),20,30)
Sprite_2.rect.x,Sprite_2.rect.y = random.randint(0,SCREEN_WIDTH - Sprite_2.rect.width),random.randint(0,SCREEN_HEIGHT-Sprite_2.rect.height)
all_sprites.add(Sprite_2)

running, won = True,False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

        if not won:
            keys = pygame.key.get_pressed()
            x_change = (keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]) 
            y_change = (keys[pygame.K_DOWN]-keys[pygame.K_UP]) 
            Sprite_1.move(x_change,y_change)
        if Sprite_1.rect.colliderect(Sprite_2.rect):
            all_sprites.remove(Sprite_2)
            won = True

        screen.
      