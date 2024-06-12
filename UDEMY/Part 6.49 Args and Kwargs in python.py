def myfunc(a,b,c=0):
    return sum((a,b,c))
print(myfunc(1,2,3))
#Vậy nếu truyền nhiều hơn 3 biến vào hàm thì sao ? -> lỗi vậy mình sử dụng *args như truyền một tuple động có thể truyền bất kì biến nào 

def func_sum(*aargs):
    return sum(aargs)
#def func_sum(*aargs):
#    for i in aargs:
#       

print(func_sum(1,2,3,4,5))

def func_args(*aargs):
    print(aargs)

func_args(1,2,3,4,5)

#**kwargs
def func_kwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('Cant find')

func_kwargs(fruit = 'Apple',price = 18)

a = {'name':'Truong','age':18}
print (a['name'])
[123].append
def func_args_kwargs(*a, **b):
    print(a)
    print(b)
    print('I would like {} {}'.format(a[0], b['food']))
func_args_kwargs(1,2,3,food = 'noodle')

def myeven(*args):
    a = []
    for i in args:
        if i %2 == 0:
            a.append(i)
    return a
print(myeven(1,2,3,4,5,6))

def myfunc(a):
    b = ''
    for i,j in enumerate(a):
        if i %2 == 0 :
            b += j.upper()
        else :
            b += j.lower()
    return b