
def func(x,n):
    res=0
    xi=x
    for i in range(1,n+1):
        res+=xi
        xi*=x
    return res

print('f(2,3)=',func(2,3))