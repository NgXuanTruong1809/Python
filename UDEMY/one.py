#one.py
def func():
    print("Func() in one.py")
print("Top level in one.py")
#co nghĩa là nếu mình chạy trực tiếp ở file one này thì nó sẽ in ra dòng đầu, và nếu one.py được import từ một cái khác và chạy từ một file khác
#thì in ra dòng thứ 2
if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")