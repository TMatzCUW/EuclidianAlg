import timeit

@profile
def GCD_loop(n, m):
    if m == 0:
        return n
    l = n % m
    while l > 0:
        n = m
        m = l
        l = n % m
    return m

@profile
def GCD_recur(n, m):
    if m == 0:
        return n
    else:
        l = n % m
        n = m
        m = l
        return GCD_recur(n, m)

def testloop():
    GCD_loop(123456789, 123456)

def testrecur():
    GCD_recur(123456789, 123456)

testloop()
testrecur()
#print(timeit.Timer(testloop).timeit(number=100))
#print(timeit.Timer(testrecur).timeit(number=100))

