import pygame

class Piece():

    def __init__(self, player, piece_type):
        self.player = player
        self.piece_type = piece_type
        self.image = pygame.image.load(f"resources/pieces/{player}{piece_type}.png")
        self.image_rect = self.image.get_rect()

    
    def paint(self, screen, x, y):
        screen.blit(self.image, (x, y))

