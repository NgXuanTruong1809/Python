from math import *

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
        if mylist[i] == 3 and mylist[i+1] == 3: # mylist[i:i+2] == [3,3]
            return True
    return False
    
def myfunc8(str):
    new_str = ''
    for char in str:
        new_str += char*3
    return new_str

def myfunc9(a,b,c):
    d = a+b+c 
    if d > 21 and (a == 11 or b == 11 or c == 11): # 11 in [a,b,c]
        d = d - 10
    if d > 21 :
        return 'BUST'
    else :
        return d
'''  new wave 
def myfunc9(a,b,c):
    if sum([a,b,c]) <= 21 : 
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) - 10 <= 21 :
        return sum([a,b,c]) - 10
    else :
        return 'BUST'
'''
    
def myfunc10(mylist):
    sum69 = 0
    i = 0
    while i < len(mylist):
        if mylist[i] == 6:
            now_i = i
            for j in range(i+1, len(mylist)):
                if mylist[j] == 9:
                    i = j
                    break
            if now_i == i:
                sum69 += mylist[i]
            print(i, now_i)
        else :
            sum69 += mylist[i]
        i += 1
    return sum69
#cach 2 cua de bai nhung chi dung trong truong hop co 6 9
"""def myfunc10(mylist):
    sum69 = 0
    add = True 
    for num in mylist:
        while add:
            if num != 6 :
                sum69 += num
                break
            else :
                add = False
        while not add:
            if num != 9 :
                break
            else : 
                add = True
    return sum69"""

def myfunc11(mylist):
    count = 0
    for num in mylist:
        if num == 0:
            count += 1 
        elif num ==7 and count >= 2:
            count += 1
            return True
        elif num ==7 and count <2 :
            count = 0
    return False
#cach 2 cua de bai nhung sai truong hop 0 7 0 7 -> van dua ra True nhung neu code cua minh se ra fall
"""def myfunc11(mylist):
    code = [0,0,7,'x']
    for num in mylist:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1"""
#a = []
#print (a[0]) tra ra loi vi khong co phan tu 0
def is_prime(num):
    if num < 2 :
        return False
    for i in range(2,int(sqrt(num))+1):
        if num %i == 0:
            return False
    return True
def myfunc12(num):
    count = 0 
    for i in range(2,num+1):
        if is_prime(i):
            count += 1
    return count

#Ham cua ho
def count_prime(num):
    if num < 2 :
        return 0
    prime = [2] #ham chua so nguyen to dau tien khong check so 2 vi su dung so 3 de tang khoang cach len 2 -> luon la so le
    x = 3 #bat dau check tu so 3 
    while x <= num :
        #check x co phai so nguyen to khong '
        for i in range(3,x,2):  #co the thay the range() thanh prime -> vi check 1 so co phai so nguyen to khong thi co the check no co chia het cho nhung so nguyen to nho hon k
            if x%i == 0 :   #neu kphai so nguyen to thi dua so x = x+2 (cho vong lap tiep theo) va break vong for
                x += 2
                break
        else:   #neu vong for khong duoc break thi se an vao else -> la so nguyen to
            prime.append(x)
            x += 2
    
    return prime.__len__()

print(count_prime(100))