# sử dụng Escape Sequence
print('\neu mot ngay nao do') 
print('\\neu mot ngay nao do') #đang muốn in ra là \neu mot ngay nao do
#đặt vấn đề : nếu thao tác với các file trên hệ thống ? nó sẽ là D:a/avb ... có dấu / và sau nó có thể là t .... -> sử dụng chuỗi trần
print(  r'\nguyen xuan truong') #Và bạn sẽ phải sử dụng chuỗi trần này một cách thường xuyên, đặc biệt là khi bạn làm việc với BIỂU THỨC CHÍNH QUY (Regular Expression)

#toán tử + (toán tử rất được hay sử dụng trong việc nối các chuỗi.)
s = 'hello' + ' python'
s += ' xuan truong'
print(s)

#toán tử *  ( toán tử này giúp tạo ra một chuỗi nhờ lặp đi lặp lại chuỗi với số lần bạn muốn.)
s = 'truong '
s = s * 2
print(s)
print('abc' * 0) # bất cứ chuỗi nào nhân với 0 cũng đều có kết quả là ‘’
print('abc' * -2) # đối với số âm cũng sẽ trả về một chuỗi ‘’

#toán tử in (Kết quả sẽ là True nếu chuỗi s xuất hiện trong chuỗi A. Ngược lại sẽ là False. )
a = 'truong'
b = 't'
print(a in b)
print(b in a)

#các toán tử so sánh với chuỗi
print('ă' < 'â')  # vì ‘ă’ đứng sau ‘â’ trong bảng mã Unicode trả ra False
print('a' > 'b')  # vì ‘b’ đứng sau ‘a’ trong bảng mã Unicode trả ra False
print( 'ac' > 'abc' ) # Ở kí tự thứ hai (có chỉ số index là 1) thì ‘c’ > ‘b’ True
print( 'z' > 'abcdefz' ) # Kí tự đầu tiên: ‘z’ > ‘a’ True
print( 'abc' < 'b' ) # Kí tự đầu tiên: ‘z’ > ‘a’ True
print( 'ab' < 'abc' ) # Đã xét hết 2 cặp kí tự, nhưng không tìm thấy sự khác nhau, chương trình so sánh độ dài của 2 chuỗi True
# Để xem vị trí của một kí tự trong bảng mã Unicode, ta sử dụng hàm ord()
print (ord('t'))

#<chuỗi>[vị trí]
# cắt chuỗi <chuỗi>[vị trí bắt đầu : vị trí dừng] 
s = 'abc xyz'
print (s[1:5])  # cắt từng kí tự có vị trí từ 1 đến 4 ‘bc x’
# s[-4: -1]  # cắt từng kí tự có vị trí từ -4 đến -2 ‘ xy’
# s[1: -1]  # cắt từng kí tự có vị trí từ 1(-6) đến 5(-2) vì vị trí dừng là 6(-1) ‘bc xy’
# s[1:None]  # lấy các kí tự có vị trí 1 đến hết chuỗi ‘bc xyz’
# s[1:]  # đặc biệt, ta chỉ cần bỏ trống, Python sẽ tự hiểu là None

# s[:]  # một cách sao chép chuỗi s
#Như đã đề cập ở trên, việc cắt chuỗi này sẽ được cắt từ trái qua phải. Vậy nếu muốn cắt từ phải qua trái thì sao?

#<chuỗi>[vị trí bắt đầu : vị trí dừng : bước]
s = 'abc xyz'
print( s[2: 5: 1])  # ta có bước bằng 1
print( s[1: 7: 2])  #  bước là 2  ‘b y’
print (s[3:1:-1])  # bắt đầu ở 3 và dừng ở 1. Các vị trí lấy là 3, 2 đáp án ‘ c’ -> cắt từ phải qua trái
print(s[4::-1]) # lấy các kí tự có vị trí từ 4 đến 0 ‘x cba’
print(s[::-1]) # một cách lấy chuỗi ngược nhờ có bước âm.

#Ép kiểu (như các ngôn ngữ khác dùng kiểu dữ liệu đằng trước)
a = 4
b = int(a)
b = float(a)
b = str(a)

#THAY ĐỔI NỘI DUNG CHUỖI
s  = 'Truong'
#s[0] = 'a'   # thay s[0] gây ra lỗi  do đó kiểu dữ liệu chuỗi là một đối tượng có thể băm (hashable object).
s = 'XT' + s[1:]
print(s)