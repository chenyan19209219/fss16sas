import random
def has_duplicates(t):
    t.sort()
    for x in range(len(t)):
        if(x!=len(t)-1):
            if(t[x]==t[x+1]):
                return True

    return False

def random_birthday_list():
    birthdays = []
    for i in range(23):
        birthdays.append(random.randint(1,365))

    return birthdays

def calculate_probability(num_of_evaluations):
    total_matches = 0
    for i in xrange(num_of_evaluations):
        bdays = random_birthday_list()
        if (has_duplicates(bdays)):
            total_matches+=1
    prob = total_matches/(num_of_evaluations*1.0)
    print 'For %d evaluations' % num_of_evaluations
    print 'for %d students' % 23
    print 'the probability was of match was %f' % prob

calculate_probability(1000)
