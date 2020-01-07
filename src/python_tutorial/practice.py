class Person():
    def __init__(self, name:str, job:str):
        self.name:str = name
        self.job:str = job
    def print(self):
        print(f'{self.name}, {self.job}')

class Author(Person):
    def __init__(self, name:str, nick:str):
        super().__init__(name, 'writer')
        self.nick:str = nick

class Librarian(Person):
    def __init__(self, name:str):
        super().__init__(name, 'librarian')

class Book():
    def __init__(self, title:str, type_:str, author:Author):
        self.title:str = title
        self.type_:str = type_
        self.author:Author = author
    def print(self):
        print(f'{self.title}, {self.type_}, {self.author.name}')

class Comics(Book):
    def __init__(self, title:str, author:Author):
        super().__init__(title, 'Comics', author)

class Horror(Book):
    def __init__(self, title:str, author:Author):
        super().__init__(title, 'Horror', author)

class Library():
    def __init__(self, name:str, librarian:Librarian, book_list:list):
        self.name:str = name
        self.librarian:Librarian = librarian
        self.book_list:list = book_list # list of Book object
    def print(self):
        print(self.name)
        self.librarian.print()
        for idx, book in enumerate(self.book_list):
            print(idx)
            book.print()
        print()

    def add_book(self, book:Book):
        self.book_list.append(book)
    def get_quantity(self) -> int:
        return len(self.book_list)
    def find_book_by_title(self, title:str) -> Book:
        for book in self.book_list:
            if book.title == title:
                return book
        print('NOT FOUND')
    def find_book_by_author_name(self, author_name:str) -> list:
        list_book = list()
        for book in self.book_list:
            if book.author.name == author_name:
                list_book.append(book)
        return list_book


a = Author('Tung', 'Nar')
b = Author('Anh', 'C')
c = Librarian('Hien')
d = Comics('Doremon', a)
e = Comics('Conan', b)
h1 = Horror('Horror 1', a)
h2 = Horror('Horror 2', a)
h3 = Horror('Horror 3', b)
book_list = [d, e, h1, h2]
library = Library('Soc Son', c, book_list)

library.print()
library.add_book(h3)
list_of_book = library.find_book_by_author_name('Anh')

for book in list_of_book:
    book.print()
