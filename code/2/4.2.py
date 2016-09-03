from swampy.TurtleWorld import *
import sys,math

sys.dont_write_bytecode=True

__author__ = "Shalini Sejwani"


def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)


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




def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def walk(t,length):
    """Walk without dropping ink
    t: Turtle
    length : length to walk
    """
    pu(t)
    fd(t,length)
    pd(t)

def flower(t,p,r,angle):
	"""Draw flower with p petals
	t:Turtle
	p:Petals
	r:radius
	angle: angle subtending arc
	"""

	for i in range(p):
	    petal(t,r,angle)
	    lt(t,360.0/p)



def petal(t,r,angle):
    """Draw petal using two arcs
    t:Turtle
    r:radius
    angle:angle subtending arc
    """
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def exercise(t):
	""" Draw the patterns shown in exercise 4.2
	t is Turltle
	"""

	t.set_pen_color("#00FF00")
	flower(t,7,60,60)


	t.set_pen_color("#0000FF")
	walk(t,120)
	flower(t,10,40,80)

	t.set_pen_color("#FF0000")
	walk(t,120)
	flower(t,20,140,20)	

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
