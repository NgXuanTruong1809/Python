# kiểu số nguyên - Một điểm đáng chú ý trong Python 3.X đó là kiểu dữ liệu số nguyên là vô hạn
a = 4 
# số thực - Số thực trong Python có độ chính xác xấp xỉ 15 chữ số phần thập phân.
pi = 3.14
# muốn chính xác cao hơn số thực thì sử dụng decimal - khai báo thư viện
from decimal import * # lấy toàn bộ nội dung của thư viện Decimal,khuyến khích dùng: from fractions import Fraction trong việc học để tạo thói quen trong công việc sau này.
getcontext().prec = 30   # lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
print (Decimal(10)/Decimal(3))
# kiểu dữ liệu này là decimal

from fractions import * # lấy toàn bộ nội dung của thư viện fractions
print(Fraction(1, 4))   # phân số với tử số là 1, mẫu số là 4.

# số phức
c = complex(2,5)
print(c)
print(c.real)
print(c.imag)

# Toán tử
    # + _ * / (// chia lấy phần nguyên) % (** mũ)

a = 3
b = (a := a + 3) + 3 #Thay đổi giá trị của biến a, đồng thời khởi tạo biến b.
# a = 6 and b = 9
print(c := 100) #Nếu cần, ta cũng có thể khởi tạo một biến bằng Assignment Expression
(t := 4) #Việc khởi tạo biến bằng Assignment Expression bên ngoài lệnh cũng được cho phép, với điều kiện phép gán được đặt trong cặp ngoặc
print(t)


