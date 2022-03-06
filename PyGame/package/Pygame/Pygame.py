
import pygame
run = True
width = 800
height = 200
pygame.init()
screen =pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 55)
text = font.render("Welcome to Paygame", True, (245, 245, 245))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height())))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.quit\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False