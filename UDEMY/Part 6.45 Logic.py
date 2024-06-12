def check_chanle(number):
    return number%2==0

def check_even_list(num_list):
    sochan = []
    for i in num_list:
        if(i%2==0):
            sochan.append(i)
        else:
            print('cc')

check_even_list([1,2,3])
#Tuple unpacking with Python function 
work = [('Xtruong',500),('HoangTuyen',300),('VanTien',250)]
def check_best_eng(work):
    max_hour = 0 
    best_eng_name = ''
    for name, hours in work:
        if(hours > max_hour):
            max_hour = hours
            best_eng_name = name
    return (best_eng_name,max_hour)
result = check_best_eng(work)
print(result)

name, time = check_best_eng(work)
print(name)
print(time)