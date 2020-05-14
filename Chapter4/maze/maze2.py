import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

class Maze: 
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, 'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == "S":
                    self.startRow = rowsInMaze
                    self.startCol = col
            rowsInMaze = rowsInMaze +1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

    self.rowsInMaze = rowsInMaze
    self.columnsInMaze = columnsInMaze
    self.xTranslate = -columnsInMaze/2
    self.yTranslate = rowsInMaze/2
    self.t = turtle.Turtle()
    self.t.shape('turtle')
    self.wn = turtle.Screen()
    self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                   self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)





def searchFrom(maze,startRow,startColumn):
    maze.updatePosition(startRow,startColumn)



myMaze = Maze('maze2.txt')
myMaze.drawMaze()