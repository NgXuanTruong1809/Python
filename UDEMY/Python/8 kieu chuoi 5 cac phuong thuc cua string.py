#<chuỗi>.split(sep=None, maxsplit=-1) Trả về một list (kiểu dữ liệu sẽ được Kteam giới thiệu ở bài KIỂU DỮ LIỆU LIST) bằng cách chia các phần tử bằng kí tự sep.
'''Nếu sep mặc định bằng None thì sẽ dùng kí tự khoảng trắng.
Nếu maxsplit được mặc định bằng -1, Python sẽ không bị giới hạn việc tách, còn không, Python sẽ tách với số lần được cung cấp thông qua maxsplit.'''

#<chuỗi>.split(sep=None, maxsplit=-1) Công dụng: cũng hoàn toàn như phương thức split, có điều là việc tách từ bên phải sang trái

#<chuỗi>.splitlines(keppends=False) Công dụng: hoàn toàn giống với phương thức split, nhưng các phần tử được chia tách bằng “\n” (xuống dòng). 
# Nếu keppends được cung cấp giá trị True, các phần tử khi được phân tách cũng sẽ có kí tự “\n” theo sau.

#<chuỗi>.partition(sep) Công dụng: Trả về một tuple với 3 phần tử. Các phần tử đó lần lượt là chuỗi trước chuỗi sep, sep và  chuỗi sau sep. 
# Trong trường hợp không tìm thấy sep trong chuỗi, mặc định trả về giá trị đầu tiên là chuỗi ban đầu và 2 giá trị kế tiếp là chuỗi rỗng.

#<chuỗi>.rpartition(sep) Công dụng: Cách phân chia giống như phương thức partition nhưng lại chia từ phải qua trái. 
# Và với sep không có trong chuỗi thì sẽ trả về 2 giá trị đầu tiên là chuỗi rỗng và cuối cùng là chuỗi ban đầu.

#<chuỗi>.count(sub, [start, [end]]) Công dụng: Trả về một số nguyên, chính là số lần xuất hiện của sub trong chuỗi. Còn start và end là số kĩ thuật slicing (lưu ý không hề có bước).

#<chuỗi>.startswith(prefix[, start[, end]]) Công dụng: Trả về  giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix. Ngược lại là False. 
# Hai yếu tố start, end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.

#<chuỗi>.endswith(prefix[, start[, end]])   Công dụng: Trả về  giá trị True nếu chuỗi đó kết thúc bằng chuỗi prefix. Ngược lại là False.
# Hai yếu tố start end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.

#<chuỗi>.find(sub[, start[, end]])  Công dụng: Trả về một số nguyên, là vị trí đầu tiên của sub khi dò từ trái sang phải trong chuỗi. Nếu sub không có trong chuỗi, kết quả sẽ là -1.
#  Vẫn như các phương thức khác, start end đại diện cho slicing và ta sẽ tìm trong chuỗi slicing này.

#<chuỗi>.rfind(sub[, start[, end]]) Công dụng: Tương tự phương thức find nhưng tìm từ phải sang trái

#<chuỗi>.index(sub[, start[, end]]) Công dụng: Tương tự phương thức find. Nhưng khác biệt là sẽ có lỗi ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu

#<chuỗi>.rindex(sub[, start[, end]])    Công dụng: Tương tự phương thức rindex. Và cũng khác ở điểm là sẽ có ValueError nếu không tìm thấy chuỗi sub trong chuỗi ban đầu

#<chuỗi>.islower() <chuỗi>.isupper() <chuỗi>.istitle() <chuỗi>.isidentifier()   <chuỗi>.isdigit()   <chuỗi>.isspace()

#import keyword  keyword.iskeyword(<chuỗi>) Công dụng: Trả về True nếu chuỗi đó tương ứng với một từ khóa. VD class, def ...