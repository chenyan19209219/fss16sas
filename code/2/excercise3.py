def right_justify(str):
    for x in xrange(70):
        str = " "+str
    return str

str = right_justify('Sneha')
print(str)
