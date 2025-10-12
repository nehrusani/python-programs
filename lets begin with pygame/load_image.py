import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')
background_image = pygame.transform.scale(pygame.image.load('background.jpeg').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))
flower_image = pygame.transform.scale(pygame.image.load('flower.jpeg').convert_alpha(),(200,200))
flower_rect = flower_image.get_rect(center = (SCREEN_WIDTH // 2,SCREEN_HEIGHT// 2 - 30))
text = pygame.font.Font(None,36).render('mom and dad')