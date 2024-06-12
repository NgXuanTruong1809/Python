a = 'My team is %s %s'%('MinhDV','PhongHQ')
print(a)
b = '%s %s'
print(b%('a','b'))
#%d và %.2f 2 chữ số phần thập phân là int và float
XC = 'Nguyen Xuan Chuong'
XT = 'Nguyen Xuan Chuong'
print(f'{XC} - DZ')	#f để format truyền biến biến XC 
print(f'{XC} + {{XT}}')
print('a: {},b: {}'.format(1,2))
print('a: {1},b: {2},c: {0}'.format(1,2,'3'))	## có thể truyền dư có thể dùng số nào cũng được -> k theẻ truyền thiếu
print('1: {one},2: {two}'.format(one='69', two= 2))
# căn lề trái căn lề phải căn giữa với c là kí tự muốn thay thế vào chỗ trống để null nếu muốn là dấu cách
print('{:^10}'.format('abc'))
print('{:<10}'.format('abc'))
print('HAHA {:>10}'.format('abc'))