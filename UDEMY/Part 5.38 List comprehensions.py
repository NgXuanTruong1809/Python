mystring = 'Hello'
mylist = []

for i in mystring:
    mylist.append(i)
# cach 2 
mylist =[letter for letter in mystring]

mylist =[num**2 for num in range(5)]

mylist =[num**2 for num in range (10) if num % 2 == 0]

#VD 
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp+32) for temp in celcius]

mylist =[num**2 if num % 2 == 0 else 'hehe' for num in range (10) ]

mylist =[]
for i in [1,2,3]:
    for j in [1,10,100]:
        mylist.append(i*j)
mylist = [x*y for x in [1,2,3] for y in [1,10,100]]
