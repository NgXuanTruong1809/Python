# Biến toàn cục
counter = 0

def increment():
    global counter  # Khai báo rằng chúng ta sẽ sử dụng biến toàn cục counter
    counter += 1

print("Trước khi gọi hàm increment:", counter)  # Output: 0
increment()
print("Sau khi gọi hàm increment lần 1:", counter)  # Output: 1
increment()
print("Sau khi gọi hàm increment lần 2:", counter)  # Output: 2
