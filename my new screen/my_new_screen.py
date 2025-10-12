import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
done = False
font = pygame.font.SysFont(None, 48)
text = font.render("happy karvachuth", True, (255, 255, 255))
try:
    image = pygame.image.load("karva.jpeg")
except pygame.error:
    image = None

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    window.fill((100, 100, 100))
    window.blit(text, (100, 220))
    if image:
        window.blit(image, (0, 0))  # Draw image at (0, 0) if loaded
    pygame.display.flip()