mylist = [1,2,3,4,5]
from random import shuffle
shuffle(mylist) #Ham nay chi su dung tai cho cua no tuc la minh khong the gan no cho thang khac
print(mylist)

result = shuffle(mylist)    #tra ra null
print(result)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(mylist)
print(result)

guess = [1,2,3]
a = shuffle_list(guess)
print(guess)
print(a)

guess1 = [1,2,3]
a1 = guess1.copy()
shuffle(a1)
print(guess1)
print(a1)

b = [1,2,3]
print(sum(b))