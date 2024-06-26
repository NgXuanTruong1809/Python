try:
    # Mã có thể gây ra ngoại lệ
    pass
except SomeException:
    # Mã xử lý ngoại lệ
    pass
else:
    # Mã chỉ được thực thi nếu không có ngoại lệ xảy ra trong khối try
    pass
finally:
    # Mã luôn được thực thi, bất kể ngoại lệ có xảy ra hay không
    pass

try:
    number1 = 1
    number2 = '2'
    print (number1 + number2)
    print('something happend')
except:
    print('You look like arent adding correctly')
else: 
    print('ADD ok')



