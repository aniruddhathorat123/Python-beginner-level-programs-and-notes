# Performance measure using `Timeit` module
# given are the different ways to calculate prime numbes between 1 to gien range.
# their performance.
# Step : 1 convert each module to test into the fucntion as show in below.
# can add return statement.
import timeit
def test1(): 
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)

def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]    

def test3():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return(1)


# step2: add statements as per folowing:
# `number=` number of times givne function should run.
print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))

#OP: 
# 0.685999870300293
# 0.687999963760376
# 0.03399991989135742
# so, 3rd alog is working faster as comared to other 2 alogs.