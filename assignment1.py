class Book:
    def __init__(self, title, author, genre):
        self.title = title 
        self.author = author 
        self.genre = genre 
        self.__is_borrowed = False 

    def get_info(self):
        return f"'{self.title}' by {self.author}"
    
    def borrow_book(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"You can borrow'{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False 
            print(f"'{self.title}' has been returned.")

        else:
            print(f"'{self.title}' was not borrowed.")

    def is_borrowed(self):
        return self.__is_borrowed
    

class EBook(Book):
    def __init__(self, title, author, genre, file_size):
        super().__init__(title, author, genre)
        self.file_fize = file_size 

    def  get_info(self):
        return f"'{self.title}' by {self.author}({self.file_fize} MB)"
    
    def download(self):
        print(f"Downloading '{self.title}'... {self.file_fize}MB file ready.")

Physical_book = Book("Yetekolefebet kulf", "Dr Mihret Debebe", "Fiction")
ebook = EBook("melos", "Yismake worku", "Fiction", 4)

print(Physical_book.get_info())
print(ebook.get_info())