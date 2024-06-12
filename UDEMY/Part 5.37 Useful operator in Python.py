for i in range(1,10,2):
    print(i)
print(list(range(0,11,2)))

count = 0
word = 'xtruong'
for i in word:
    print(i)
    count += 1
print ('total: {}'.format(count)) 
#Ham liet ke -> dua ra mot tuple
for i in enumerate(word):
    print(i)
for i, j in enumerate(word):
    print(i)
    print(j)
#Ham zip -> Nguoc lai so voi liet ke 
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [100,200,300]

for i in zip(list1,list2,list3):
    print(i)
for a,b,c in zip(list1,list2,list3):
    print(b)
 
print( list(zip(list1,list2,list3)))

new_var = 'k',2
dict([new_var])

print ('x' in [1,2,3])
print ('x' in ['x','y'])
print(min(list1))
print(max(list1))

from random import shuffle
mylist = [1,2,3,4,5]
shuffle(mylist)

from random import randint
a = randint(0,10)