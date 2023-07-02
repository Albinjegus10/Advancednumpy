from numba import njit
@njit
def func_with_numba():
    res=[]
    for a in range (10000):
        for b in range(10000):
            if (a+b)%11 ==0:
                res.append((a,b))


func_with_numba()





