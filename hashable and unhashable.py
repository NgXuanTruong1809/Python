a = id('truong')
print(a)
#Khác chương trình khác địa chỉ
print(id('truong'))
#chuỗi nó sẽ là một hasahable vì nó có một cái địa chỉ cố định không thay đổi được, còn clist nó sẽ khác dữ liệu nhau nên có thay đổi
#kiểu int sẽ không thay đỏi
n = 69
print(n+1)
print(n.__add__(1))
print(n.__sub__(2))
print(n.__mul__(2))
print(n.__neg__())
print(n)
#Nếu sử dụng toán tử += sẽ không làm thay đổi địa chỉ  nếu làm s1 = s1 + ... thì là gán địa chỉ mới