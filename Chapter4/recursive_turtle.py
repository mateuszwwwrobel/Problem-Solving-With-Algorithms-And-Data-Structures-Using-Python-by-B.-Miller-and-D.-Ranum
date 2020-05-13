

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        myTurtle.forward(lineLen)
        myTurtle.left(10)
        drawSpiral(myTurtle,lineLen-1)


#drawSpiral(myTurtle,125)
#myWin.exitonclick()

t = turtle.Turtle()


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)

tree(100,t)
myWin.exitonclick()