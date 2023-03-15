class Board:
    def __init__(self, size):
        self.board = [[None for x in range(size)] for y in range(size)]

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