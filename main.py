import pygame
import sys
from Board import Board

pygame.init()
background = pygame.image.load("resources\GreenChessboard600x600.png")
window = pygame.display.set_mode((600, 600))
board = Board(8)


# TEMPORARY 
wking = pygame.image.load("resources\white\wking.png")
image_rect = wking.get_rect()
image_rect.center = (300, 300)
# END OF TEMPORARY

mouse_pressed = False
# Main game loop
while True:
    window.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and image_rect.collidepoint(event.pos):
                mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_pressed:
                image_rect.center = pygame.mouse.get_pos()

    window.blit(wking, image_rect)
    pygame.display.update()
