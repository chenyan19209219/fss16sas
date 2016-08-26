import utest, random
@utest.ok

def random1():
	a = random.random()
	b = random.randint(1, 100)
	return a, b

