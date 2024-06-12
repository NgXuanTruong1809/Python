#name = input('Name input: ')
def name_of_funtion(name):  #su dung def la khai bao ham
    '''
    Docstring explains function
    '''
    print(f'Hello {name}')
name_of_funtion('hehe')
#Ham -> co return tra ve cai gi do va thu tuc la thuc hien cai gi do    
def plus_func(num1, num2):
    return num1+num2
total = plus_func(1,2)
print(total)

#co the de gia tri mac dinh cho cac bien
def name_of_funtion_plus(name = 'XTR'):  #su dung def la khai bao ham
    print(f'Hello {name}')
name_of_funtion_plus()
name_of_funtion_plus('BIEN')