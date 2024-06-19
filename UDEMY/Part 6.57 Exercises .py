from math import *

def vol(rad):
    return (4/3)*pi*(rad**3)

def ran_check(num, low, high):
    return  low <= num <= high 

def up_low(s):
    low = 0 
    up = 0
    print(f'Original string : {s}' )
    for i in s:
        if i.isupper():
            up += 1 
        else :
            low +=1
    print(f'Upper case characters : {up}' )
    print(f'Lower case characters : {low}' )

def unique_list(lst):
    a = set(lst)
    return list(a)

def multiply_(numbers):
    x =  1
    for i in numbers:
        x *= i
    return x

def palindrome(s):
    return s[:] == s[::-1]

import string 
def ispangram(str1, alphabet = string.ascii_lowercase):
    
    for i in str1: 
        alphabet = alphabet.replace(i, '')
    return alphabet == ''

print(ispangram('the quick brown fox jumps over the lazy dog'))
