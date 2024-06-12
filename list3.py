a = [1,2,3,4,5,6,7,8,9]
c = a.count(1)  #Dem so lan xuat hien cua so 1 trong count
c = a.index(1)  #Vi tri dau tien cua phan tu 1 trong list neu khong  co so ton tai thi loi
c = a.copy()    #Tao ra mot ban sao -> tuong tu constructor list  -> khong cung tro vao 1 vi tri
c = a.clear()   #xoa tat ca gia tri mang    -> mang a gio la mang rong -> c = a Nhung se tra ra None -> rong vi no khong con dinh dang den a

print(c)
print(a)

a.append(1)
a.append([2,3]) #Them thang vao list 
print(a)
a.extend([4,5,[6,7]])   #Them nhung ke thua chuoi
print(a)
a.insert(1,9)   #Them phan tu 9 vao vi tri 1 
print (a)
a.pop(1)    #Lay ra vi tri thu 1 trong vi du la 9   pop khong co tham  so -> bo phan tu cuoi cung
print (a)
a.remove(1) #Bo di phan tu da utien co gia tri 1 
print (a)
a.reverse() #Dao nguoc list
a = [1,4,6,2]
a.sort() #Sap xep 
a.sort(reverse=True)    #Sap xep nguoc, o trong sort co 2 tham so key va reverse    
#va phan tu list sap xep phai cung kieu du lieu khong duoc list trign list