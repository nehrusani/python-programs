import pygame
import random
pygame.init()
Sprite_Color_Change_Event = pygame.USEREVENT + 1
Background_Color_Change_Event = pygame.USEREVENT + 2
Blue = pygame.color('blue')
lightblue = pygame.color('lightblue')
darkblue = pygame.color('darkblue')

Yellow = pygame.color('yellow')
Megenta = pygame.color('megenta')
orange = pygame.color('orange')
white = pygame.color('white')

class Sprite (pygame.sprite.Sprite) :
    def __init__(self,color,height,width) :
        super().__init__()
        self.image =pygame.surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundry_hit= False
        if self.rect.left <= 0 or self.rect.right >= 500 :
            self.velocity[0] = -self.velocity[0]
            boundry_hit = True
        if  self.rect.top <= 0 or self.rect.bottom >= 400 :
            self.velocity[1] = -self.velocity[1]
            boundry_hit = True
        if boundry_hit:
            # pick a new color for the sprite and fill its surface
            new_color = random.choice([Blue, lightblue, darkblue, Yellow, Megenta, orange, white])
            self.image.fill(new_color)
            # post events so the rest of the program can react (include color in event)
            pygame.event.post(pygame.event.Event(Sprite_Color_Change_Event, {'color': new_color}))
            pygame.event.post(pygame.event.Event(Background_Color_Change_Event, {'color': random.choice([Blue, lightblue, darkblue, Yellow, Megenta, orange, white])}))