import utest

@utest.ok

def MyName():
    return 'Ankur'

@utest.ok
def failcase():
    assert 'ankur' == 'sneha'
    