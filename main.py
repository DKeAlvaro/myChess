import pygame
import sys
from Board import Board
from Piece import Piece

# Initialize Pygame
pygame.init()

# Set up game window
screen = pygame.display.set_mode((600, 600))
background = pygame.image.load("resources/GreenChessboard600x600.png")

# Create pieces and game board
black_king = Piece("b", "king")
black_pawn = Piece("b", "pawn")
black_pieces = [black_pawn, black_king]
board = Board(8)

# Initialize selected piece
selected_piece = None

# Main game loop
while True:
    # Fill background
    screen.blit(background, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for piece in black_pieces:
                if event.button == 1 and piece.image_rect.collidepoint(event.pos):
                    selected_piece = piece
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_piece = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_piece is not None:
                selected_piece.image_rect.center = pygame.mouse.get_pos()

    # Draw pieces to screen
    for piece in black_pieces:
        piece.paint(screen, piece.image_rect.x, piece.image_rect.y)

    # Update display
    pygame.display.update()
