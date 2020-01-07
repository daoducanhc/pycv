class Book():
    def __init__(self, n_pages:int):
        self.n_pages = n_pages

    def print(self):
        print(self.n_pages)

b = Book(3)
b.print()


class Comics(Book):
    def __init__(self):
        super().__init__(5)
        self.name = 'Comics 1'

    # def print(self):
    #     super().print()
    #     print(self.name + str(self.n_pages))

c = Comics()
c.print()
