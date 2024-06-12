def myfunc(a,b):
    if (a %2 ==0 and b%2 ==0):
        return min(a,b)
    else : 
        return max(a,b)
    
def myfunc1(a):
    return a.split()[0][0] == a.split()[1][0]

def myfunc2(a,b):
    return a+b ==20 or a == 20 or b == 20
      
def myfunc3(a):
    return (7 - a) * 2 + 7

def myfunc4(a):
    return  a[0].upper() + a[1:3] + a[3].upper() + a[4:]
#hoac su dung print('a'.capitalize()) 

def myfunc5(a):
    return ' '.join(a.split()[::-1])

def myfunc6(n):
    #return (a >= 90 and a<= 110) or (a>= 190 and a<= 210)
    return abs(100-n) <= 10 or abs(200-n) <= 10

def myfun7(mylist):
    for i in range(len(mylist)-1):
        if mylist[i] == 3 and mylist[i+1] == 3:
            return True
    return False
    
print(myfun7([1,3,1,3]))


