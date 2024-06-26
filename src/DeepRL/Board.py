from .Cell import Cell


class Board() :
    """ Represents a board full of cells """
    
    def __init__(self) :
        """ Creates a new board with a height and width of 3 """
        self.__grid = [[Cell() for col in range(3)] for row in range(3)]
    
    
    def copyGrid(self) :
        """
        Retrives an independant copy of the grid.
        :returns: grid The grid representing the board
        """
        copy = [[self.__grid[y][x].getCopy() for x in range(3)] for y in range(3)]
        return copy
    
    
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
        for y in range(3) :
            print('+-+-+-+')
            toPrint = '|'
            for x in range(3) :
                toPrint += self.getCell(x, y).getCellRepresentation() + '|'
            print(toPrint)
        print('+-+-+-+')
