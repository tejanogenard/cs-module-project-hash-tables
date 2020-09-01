# Your code here

import math 
import random
import time 

start_time = time.time()

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # we want to store our input inside our cache 
    # we want to caclulate our product 
    # with our product calculate the factorial of the product 
    # finally return our value pair 

    if (x, y) not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        cache[(x, y)] = v % 982451653

    return cache[(x,y)]






# Do not modify below this line!

for i in range(500000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')

print("--- %s seconds ---" % (time.time() - start_time))
