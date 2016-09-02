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

world = TurtleWorld()
bob = Turtle()
length = 200
drawCircle(bob,180)
