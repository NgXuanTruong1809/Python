a = [1,2,3, 'Truong']
print(a)
b = [[[1],[2]],[3]] #nhiều list trong list
print(b)
#List giới hạn ngoặc vuông , phần tử cách nhau bằng dấu phẩy, chứa mọi kiểu dữ liệu
#List có thể chứa list như ví dụ b 
c = []	#c list rỗng
d = [i for i in range(5)]   #trả ra list từ 0 -> 4
print(d)
#Range trong pỷthon (a,b) -> từ a đến b-1
a  = list([1,2,3])      #constructor list   -> list(iterable)      interable bao gom list, chuoi (Tap hop nhieu phan tu)
print(a)
a  = list('Truong') #Su dung constructor dua ra list cac ki tu trong chuoi
print(a)
a = [1,2]
a += [3,4]      #Toan tu
print(a)
print(a*2)      #Toan tu nhan chi nhan duoc voi 1 so
e = [[n,n+1,n+2] for n in range(1,4) ]  #Cu phap for trong list VD nay dua ra list trong list
print(e)
b = 1 in a #Toan tu in (Kiem tra cai gi co nam trong chuoi kia k) -> tra ra true flase
print(b)
b = a[0]
print(b)
##############
a = [1,2,3,[4,5]]
b = a[3][0]
b = a[-1]   #vi tri cuoi cung
b = a[1:3]  #Lay vi tri 1 2 chu khong lay 3
b = a[:3]   #Lay vi tri 0 1 2 
b = a[3:]
b = a [::-1]    #Lay y ngueyn nhung dao nguoc lai
b = a[:-1] #lay tu dau den gia tri truoc gia tri -1 la [4,5]
b = a[::]   ##Lay het
print (b)