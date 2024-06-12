a = [1,2,'a',[3,4]]
a [1] = 'Xuan truong'
b = a[1]
print(a)
print(b)
#list co the thay doi gia tri khong giong voi chuoi string
###Ma Tran
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a[0][-1])
print(a[1])
print(a[2])
###
a = [1,2,3]
b = a
print(a)
print(b)
b[0] = 'Truong'
print(a)
print(b)
#Khong duoc gan list nay = list kia neu khong thay doi 1 cai no se thay doi cai con lai -> 2 list tro vao cung mot noi
a = [1,2,3]
b = list(a)    #clone list b = a khac voi viec gan thang a = b 
print(a)
print(b)
b[0] = 'Truong'
print(a)
print(b)
###
a = [[1,2,3],[4,5,6]]
b = list(a)    #clone list b = a khac voi viec gan thang a = b 
print(a)
print(b)
#b[0][0] = 'Truong'  Ca 2 cung bi thay doi vi list [1,2,3] trong list a chua duoc clone
b[0] = 'Truong' #Truong hop nay thi co the su dung
print(a)
print(b)