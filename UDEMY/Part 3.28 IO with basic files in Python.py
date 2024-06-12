myfile = open(r'D:\Python\UDEMY\myfile.txt')       #bạn sẽ hay gặp lỗi vì toán tử \ vì vậy nhớ sử dụng chuỗi trần "r"
print(myfile.read())
print(myfile.read()) # lần thứ 2 đọc không ra vì có con trỏ đọc file từ đầu đến cuối vậy nếu muốn đọc lại thì phải reset con trỏ về đầu

print(myfile.seek(0)) # đưa về dòng thứ mấy -> đưa về dòng đầu 
print(myfile.read())

#vậy lấy 1 chuỗi để nhận giá trị của file 
print(myfile.seek(0)) # đưa về dòng thứ mấy -> đưa về dòng đầu 
contents = myfile.read()
print(contents)

#Đưa file thành một chuỗi
print(myfile.seek(0)) # đưa về dòng thứ mấy -> đưa về dòng đầu 
print(myfile.readlines())

#mở file xong nếu không dùng phải đóng vì nếu có thể đọc 1 file cùng tên khác ổ nó sẽ báo đang sử dụng file này
myfile.close()

#hoặc nếu không mở file trực tiếp có thể gán file đó thành 1 biến
with open(r'D:\Python\UDEMY\myfile.txt') as my_new_file:
    contents_new = my_new_file.read()
print(contents_new)

#ghi đè hoặc ghi vào file 
with open(r'D:\Python\UDEMY\myfile.txt', mode='a') as myfile:
    myfile.write('\n4 lines')
with open(r'D:\Python\UDEMY\myfile.txt', mode='r') as myfile:
    print(myfile.read())
with open(r'D:\Python\UDEMY\new_myfile.txt', mode='w') as myfile:
    print(myfile.write('I JUST CREATED THIS FILE'))
'''
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'''