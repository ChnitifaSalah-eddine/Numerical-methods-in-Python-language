def puissance(x,n):
    res=x
    for i in range(n-1):
        res*=x
    return res

def func(x,n):
    res=0
    for i in range(1,n+1):
        res+=puissance(x,i)
    return res

print('f(2,3)=',func(2,3))