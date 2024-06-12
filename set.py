#seet được giới hạn bởi cặp {}, được phân cách bởi dấu phẩy, không chứa nhiều hơn 1 phần tử trùng lặp
# phần tử của set là hashable object -> nhưng nó không phải hashable, ví dụ có thể chứa tuple không thể chứa list kể cả list có ở trong tuple
#Vậy nó không thể chứa chính nó
a = {'truong','xtruong',69}
print(a)

a = {1,1,1}
print(a)
a= {}
print(type(a))
#bạn không tthể tạo 1 empty set bằng {} chỉ có thể dùng constructor
print({1,2,3}- {1,2})
print({1,2,3}- {1,2,3,5,6})
print({1,2,3} & {1,2,3,5,6}) #Toán tử AND 
print({1,2,3} | {1,2,3,5,6}) #Toán tử OR 
print({1,2,3} ^ {1,5,6}) #Toán tử XOR = OR - AND 

set1 = {3,2,4,1}    #Set tự đoọng sắp xếp 
set1.pop()      #Đôi với list lấy ra phần tử cuối cùng với tham số rỗng còn với set là lấy ra phần tử đầu 
print(set1)

set1.discard (5)    #giống remove nhưng nếu k có phần tử 5 thì sẽ không báo lỗi