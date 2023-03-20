from Piece import Piece


class Board:

    def __init__(self):
      
        # Create pieces and game board
        self.white_pawn = Piece("w", "pawn")
        self.white_knight = Piece("w", "knight")
        self.white_bishop = Piece("w", "bishop")
        self.white_rook = Piece("w", "rook")
        self.white_queen = Piece("w", "queen")
        self.white_king = Piece("w", "king")

        self.black_pawn = Piece("b", "pawn")
        self.black_knight = Piece("b", "knight")
        self.black_bishop = Piece("b", "bishop")
        self.black_rook = Piece("b", "rook")
        self.black_queen = Piece("b", "queen")
        self.black_king = Piece("b", "king")
        self.board = [
                        [self.black_rook, self.black_knight, self.black_bishop, self.black_queen, self.black_king, self.black_bishop, self.black_knight, self.black_rook],
                        [self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn, self.black_pawn],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [None, None, None, None, None, None, None, None],
                        [self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn, self.white_pawn],
                        [self.white_rook, self.white_knight, self.white_bishop, self.white_queen, self.white_king, self.white_bishop, self.white_knight, self.white_rook]
                    ]
        
            

    def getPiece(self, x, y):
        return self.board[x][y]

    def movePiece(self, prevX, prevY, newX, newY):
        piece = self.getPiece(prevX, prevY)
        self.deletePiece(prevX, prevY)
        self.addPiece(self, newX, newY, piece)
    
    def addPiece(self, x, y, piece):
        if self.board[x][y] == None:
            self.board[x][y] = piece
        else:
            print("There is a piece already here!")

    def deletePiece(self, x, y):
        self.board[x][y] = None