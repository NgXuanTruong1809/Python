# <chuỗi> % (giá trị thứ 1, giá trị thứ 2, .., giá trị thứ n – 1, giá trị thứ n)
s = '%s %s'
print(s%('one','two'))
print ('My name is %s.' %('Lucario'))
print('%d. That is %s problem.' %(1,'this'))
# Ngoài ra còn %r và %.<chứ số phần thập phân>f

class SomeThing:
        def __repr__(self):
                 return 'Đây là __repr__'
        def __str__(self):
              return 'Đây là __str__'
        
sthing = SomeThing() # tạo đối tượng thuộc lớp
print('%s ' %(sthing))
print('%r ' %(sthing))

# f ’giá trị trong chuỗi’
variable = 'string'
print(f'this is a {variable}')
# 1: {one}, 2: {two}, 3: {variable} đặt vấn đề Và chỉ muốn định dạng mỗi chỗ {variable} thôi thì phải làm sao?
print(f'1: {{one}}, 2: {{two}}, 3: {variable}')
# Ngoài ra, chuỗi f còn hỗ trợ một cách in giá trị khá đặc biệt, cũng như là hỗ trợ toán tử :=.
v = 1
t = 2
print(f'Two variables {v=} and {t=}')
#
print(f'Using operator := with c={(c:=3)}')

#Định dạng bằng phương thức format
print('a: {}, b: {}, c: {}'.format(1, 2, 3))
print('a: %d, b: %d, c: %d' %(1, 2, 3))

print('a: {1}, b: {2}, c: {0}'.format('one', 'two', 'three'))
print('only one value: {0}'.format('one', 'two'))
print('only one value: {1}'.format('one', 'two'))
print('same value: {0} {0}'.format('one', 'two'))

print('1: {one}, 2: {two}'.format(one = 111, two = 222))
#Dưới đây là 3 cách căn lề cơ bản của phương thức format
#Căn lề trái: {:(c)<n}
#Căn lề phải: {:(c)>n}
#Căn giữa: {:(c)^n}
'''Trong đó
c là kí tự bạn muốn thay thế vào chỗ trống, nếu để trống thì sẽ là kí tự khoảng trắng
n là số kí tự dùng để căn lề.'''


# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Kteam', 'TP HCM')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Kquiz', 'Da Lat')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)