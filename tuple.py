#được giới hạn bởi cặp ngoặc () -> gần giống list
#các phần tử của tuple được phân cách nhau bởi dấu , 
#có khả năng chứa mọi giá trị
#tốc độ truy xuất nhanh hơn list, dung lượng chiếm trong bộ nhớ nhỏ hơn list
#bảo vệ dữ liệu của bạn sẽ không bị thay đổi
#có thể dùng lạm key của dictionary
#tuple giống str và khác ít so với list
#hash obj không thể thay đổi giá trị ví dụ str 
tup = (1)   #Nếu chỉ đuaw 1 phần tử thì không được hiểu là 1 tuple
tup = (1,)  #đưa dấu phẩy vào cho nó hiểu 
tup = (i for i in range(10) if i % 2 == 0)        #neu dung thang truc tiep giong list se sai
a = tuple([1,2,3])
a = tuple((1,2,3))
a = tuple('truong')
a = tuple(tup)
print(a)
#nếu giá trị bên trong tuple là list thì -> unhashobj có thể thay đổi
list = 1, 2
print(list)