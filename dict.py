'''Dict(Dictionary) cũng là một container như list, tuple. Có điều khác biệt là những container như list, tuple có các index để phân
biệt các phần tử thì dict cũng dùng các key để phân biệt
Một dict bao gồm các yếu tố sau
Được giới hạn bởi cặp ngoặc nhọn, ngăn cách bởi dấu phẩy 
Các phần tử của dict là một cặp key-value
cặp key value được phân cách bởi dấu hai chấm
các key buộc phải là một hashobject'''
dic = {'name': 'truong', 'age': 22}
print(dic)
#có thể sử dụng set comprehension như list, tuple 
dict  = {key: value for key, value in [('name', 'truong'),('age', 22)]}
print(dic)