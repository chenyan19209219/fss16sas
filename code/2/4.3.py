from swampy.TurtleWorld import *
import sys,math

sys.dont_write_bytecode=True

__author__ = "Shalini Sejwani"



def align(t,length):
    """
    For two sections , align the turtle
    down to print the second sequence.
    :param t: Turtle
    :param length: Length to move down
    """
    pu(t)
    rt(t,90)
    fd(t,length)
    lt(t,90)
    pd(t)



def walk(t,length):
    """Walk without dropping ink
    t: Turtle
    length : length to walk
    """
    pu(t)
    fd(t,length)
    pd(t)


def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    t: Turtle
    n: number of segments
    r: length of the radial spokes
    Using : http://www.greenteapress.com/thinkpython/code/pie.py
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    The turtle starts and ends at the peak, facing the middle of the base.
    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    Using http://www.greenteapress.com/thinkpython/code/pie.py
    """
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)


def exercise(t):
	""" Draw the patterns shown in exercise 4.2
	t is Turltle
	"""

	t.set_pen_color("#00FF00")
	polypie(t,5,60)


	t.set_pen_color("#0000FF")
	walk(t,120)
	polypie(t,6,60)

	t.set_pen_color("#FF0000")
	walk(t,120)
	polypie(t,7,60)

	walk(t,100)


if __name__ =='__main__':
	world = TurtleWorld()
	ted = Turtle()
	print ted

	ted.delay = 0.004

	exercise(ted);


	# fd(ted, 100)
	# lt(ted)
	# fd(ted, 100)

	# align(ted, 180)
	# polygon(ted, 7, 70)

	wait_for_user()
