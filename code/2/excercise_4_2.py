from swampy.TurtleWorld import *

def drawSquare(bob,length):
    for i in range(4):
        fd(bob, length)
        lt(bob)
    wait_for_user()

def drawPolygon(bob,n):
    for i in range(n):
        fd(bob,100)
        lt(bob,360/n)

def drawCircle(bob,arc):
    bob.delay = 0.01
    for i in range(arc):
        fd(bob,1)
        lt(bob,1)

def drawFlower(t,noOfPetals):
    bob.delay = 0.001
    for j in range(noOfPetals):
        for i in range(180):
            fd(t,1)
            lt(t,1)
        lt(t,100)

world = TurtleWorld()
bob = Turtle()
length = 200
drawFlower(bob,5)
wait_for_user()
