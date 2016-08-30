def dash():
    print '-',

def plus():
    print '+',

def div():
    print '|',

def space():
    print ' ',

def eol():
    print

def do_four(f):
    f()
    f()
    f()
    f()

def draw_one_half():
    plus()
    do_four(dash)

def draw_onemidlast():
    draw_one_half()
    draw_one_half()
    plus()
    eol()

def draw_mid():
    div()
    do_four(space)
    div()
    do_four(space)
    div()
    eol()

draw_onemidlast()
do_four(draw_mid)
draw_onemidlast()
do_four(draw_mid)
draw_onemidlast()
