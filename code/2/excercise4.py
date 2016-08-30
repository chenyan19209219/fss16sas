def do_twice(f,str):
    f(str)
    f(str)

def do_four(f,str):
    do_twice(f,str)
    do_twice(f,str)

def print_twice(str):
    print str
    print str

do_four(print_twice,"spam")
