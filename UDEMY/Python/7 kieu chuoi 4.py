# Các phương thức biến đổi
# <chuỗi>.capitalize() - Trả về một chuỗi với kí tự đầu tiên được viết hoa và viết thường tất cả những kí tự còn lại.
print('kteaM'.capitalize())

#<chuỗi>.upper()
#<chuỗi>.lower()
#<chuỗi>.swapcase()  Trả về một chuỗi với các kí tự viết hoa được chuyển thành viết thường, các kí tự viết thường được chuyển thành viết hoa
#<chuỗi>.title()  Trả về một chuỗi với định dạng tiêu đề, có nghĩa là các từ sẽ được viết hoa chữ cái đầu tiên, còn lại là viết thường
#<chuỗi>.center(width, [fillchar]) : Trả về một chuỗi được căn giữa với chiều rộng width. 
# Nếu fillchar là None (không được nhập vào) thì sẽ dùng kí tự khoảng trắng để căn, không thì sẽ căn bằng kí tự fillchar.
#Một điều nữa là kí tự fillchar là một chuỗi có độ dài là 1.
print('abc'.center(10,'*'))
#<chuỗi>.rjust(width, [fillchar]) Công dụng: Cách hoạt động tương tự phương thức center, nhưng căn lề phải.
print('Kter'.rjust(12))
print('Kter'.rjust(12,'*'))
#<chuỗi>.ljust(width, [fillchar]) Công dụng: Cách hoạt động tương tự phương thức center, nhưng căn lề trái.
print('Kter'.ljust(12))
print('Kter'.ljust(12,'*'))
#<chuỗi>.encode(encoding=’utf-8’, errors=’strict’)   Đây là phương thức dùng để encode một chuỗi với phương thức mã hóa mặc định là utf-8.
print('ố ồ'.encode())
#<chuỗi (đã mã hóa)>.decode(encoding=’utf-8’, errors=’strict’) Công dụng: dùng để giải mã các kí tự đã được mã hóa bởi phương thức encode.
t = 'ố ồ'.encode()
print(t.decode())
#<kí tự nối>.join(<iterable>) Công dụng: Trả về một chuỗi bằng cách nối các phần tử trong iterable bằng kí tự nối. Một iterable có thể là một tuple, list,… hoặc là một iterator (Một điểm lưu ý, các phần tử trong iterable buộc phải thuộc lớp str)
print(' '.join(['1', '2', '3']))
#<chuỗi>.replace(old, new, [count]) Công dụng: Trả về một chuỗi với các chuỗi old nằm trong chuỗi ban đầu được thay thế bằng chuỗi new. Nếu count khác None (có nghĩa là ta cho thêm count) thì ta sẽ thay thế old bằng new với số lượng count từ trái qua phải.
#Nếu chuỗi old không nằm trong chuỗi ban đầu hoặc count là 0 thì sẽ trả về một chuỗi giống với chuỗi ban đầu

#<chuỗi>.strip([chars]) 
''' Công dụng: Trả về một chuỗi với phần đầu và phần đuôi của chuỗi được bỏ đi các kí tự chars. Nếu chars bị bỏ trống thì mặc định các kí tự bị bỏ đi là dấu khoảng trắng và các escape sequence. 
Một số escape sequence ngoại lệ như \a sẽ được encode utf-8. Tuy vậy, không có ảnh hưởng gì tới nội dung.'''
#<chuỗi>.rstrip() Công dụng: Cách hoạt động hoàn toàn như phương thức strip, nhưng khác là chỉ bỏ đi ở phần đuôi (từ phải sang trái)

#<chuỗi>.removeprefix([prefix]) Công dụng: Trả về một chuỗi mới, chính là chuỗi ban đầu với phần đầu đã được bỏ đi [prefix] Nếu [prefix] không xuất hiện ở phần đầu của chuỗi, phương thức removeprefix trả về chính chuỗi đó.

#<chuỗi>.removesuffix([suffix]) Công dụng: tương tự như removeprefix, nhưng nó sẽ xóa ở cuối chuỗi.