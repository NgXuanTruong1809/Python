print("5+5")
#COMMENT
string = "XuanChuong"	
a = 3
b = 4.5
c = a + b
print(c) 
e, f, g = 1, 2, 3
print(e + f  + g ) 
print(type(e))
#Python không giới hạn miền giá trị :> có thể 20 nghìn tỷ
#Số thực trong python có độ xấp xỉ chính xác khoảng 15 giá trị sau dấu phẩy -> tự động làm tròn

#Lấy toàn bộ nội dung của thư viện decimal
from decimal import*
#Lấy tối đa 30 chữ số phần nguyên và phần thập phân decimal -> mặc định của decimal là 30
getcontext().prec = 30
print(10/3)
print(Decimal(10)/Decimal(3))
