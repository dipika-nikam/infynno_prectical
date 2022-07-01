def myfunc(n):
    return lambda a: a + n


m = myfunc(3)
print(m(3))
