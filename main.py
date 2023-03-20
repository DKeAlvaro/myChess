import pygame
import sys
from Board import Board
from Piece import Piece

# Initialize Pygame
pygame.init()

# Set up game window
screen = pygame.display.set_mode((600, 600))
background = pygame.image.load("resources/GreenChessboard600x600.png")
board = Board()

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
            for i in range(8):
                for j in range(8):
                    if board.getPiece(i, j) is not None:
                        if event.button == 1 and piece.image_rect.collidepoint(event.pos):
                            selected_piece = piece
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_piece = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_piece is not None:
                selected_piece.image_rect.center = pygame.mouse.get_pos()

    # Draw pieces to screen
    for i in range(8):
        for j in range(8):
            if board.getPiece(i, j) is not None:
                x = j * 70 + 17 
                y = i * 70 + 17
                piece = board.getPiece(i, j)
                piece.paint(screen, x, y)

    # Update display
    pygame.display.update()
