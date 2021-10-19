from functools import reduce

def persistence(n, times = 0):
    return times if n < 10 else persistence(reduce(lambda x, y: x * y,[int(c) for c in str(n)]),times + 1)
