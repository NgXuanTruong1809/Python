def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

#VD 1 ham su dung voi chuoi
def splicer(mystring):
    if len(mystring) %2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Truong','Tien','Yen']
print(list(map(splicer, names)))

def check_even(num):
    return num%2==0

list_num = [1,2,3,4]
print(list(map(check_even, list_num)))

print(list(filter(check_even, list_num)))

for i in filter(check_even, list_num):  #Filter tra ve nhung cai true 
    print (i)

# Sử dụng lambda với hàm map để bình phương các phần tử trong một danh sách
squares = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Sử dụng lambda với hàm filter để lọc ra các số chẵn trong một danh sách
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(evens)  # Output: [2, 4, 6]

# Định nghĩa một hàm lambda để cộng hai số
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Sắp xếp một danh sách các tuple theo phần tử thứ hai
tuples = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


