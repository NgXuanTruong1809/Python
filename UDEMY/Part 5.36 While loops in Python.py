x = 0
while x < 5 :
    print(x)
    x += 1
    continue
else :
    print ('x da bang 5')

x = [1,2,3]
for i in x :
    pass
mystring = 'Truong'
for i in mystring:
    if i =='u':
        continue
    print(i)
for i in mystring:
    if i =='u':
        break
    print(i)

#break - Thoát khỏi vòng lặp hiện tại, continute -đi đến đầu vòng lặp bao quanh gần nhất, pass -không làm gì hết