from src.DeepRL.Cell import Cell


class Board() :
    """ Represents a board full of cells """
    
    def __init__(self) :
        """ Creates a new board with a height and width of 3 """
        self.__grid = [[Cell() for j in range(3)] for i in range(3)]
    
    
    def getCell(self, x, y) :
        """
        Retrieves the cell at position x, y
        :Param: x The collum of the cell
        :Param: y The row of the cell
        :returns: The cell at position (x, y)
        """
        return self.__grid[y][x]
    
    
    def capture(self, x, y, opp) :
        """
        Sets the owner of the cell
        :Param: x The x position of the cell
        :Param: y The y position of the cell
        :Param: opp The opponent who captured the cell
        """
        cell = self.getCell(x, y)
        cell.setOwner(opp)
    
    
    def printBoard(self) :
        """
        Print the board
        """
        pass
