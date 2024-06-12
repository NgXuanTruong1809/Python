strA = 'Nguyen Xuan Truong'
print(strA[2:None])
# khong ho tro strA[0] = 'Z'
strA = strA[None:1] + 'G' + strA[2:None] 
print(strA)
print(hash(strA))	#Mã hóa mỗi lần 1 khác 

