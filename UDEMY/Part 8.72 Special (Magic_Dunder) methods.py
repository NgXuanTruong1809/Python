from typing import Any


class Sample():
    pass

sample = Sample()

#len(sample) Khong the su dung hoac cung the print tuong tu nhu list 
print(sample)   #Tra ve dia chi luu khong nhu list hay str ... tra ra gia tri

class Book():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self) -> str:   #ham dac biet bieu dien chuoi -> co the print doi tuong cua class 
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book object has been deleted')
b = Book('Python rocks', 'Jose', 200)
print(b)
print( len(b))
#muon xoa mot doi tuong da tao ra 
del b #xoa khoi bo nho tren mau tinh
