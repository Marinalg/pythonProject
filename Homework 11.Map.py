def myfunc(a):
    return a*a

t = map(myfunc, (1,2,3,4))
print(t)
print(set(t))