lists = [1,2,3,4,5]
list_sum = 0
for list in lists:
    print(list)
    list_sum += list
    if list % 2 == 0 :
        print('So chan {}'.format(list)) 
print(list_sum)
string = 'truong'
for char in string:
    print(char)

for char in 'XTR':
    print(char)

tup = (1,2,3)
for item in tup:
    print(tup)

for i in range(3):
    print (i)
#giai nen tuple
mylist = [(1,2),(3,4),(5,6)]
for a,b in mylist:
    print(a)
    print(b)

dictionaries = {'k1':1,'k2':2}
#co the for theo dict.value() hoặc dict.key()
for i in dictionaries:
    print(i)
for i in dictionaries.items():
    print(i)
for key, value in dictionaries.items():
    print(key)
    print(value)
