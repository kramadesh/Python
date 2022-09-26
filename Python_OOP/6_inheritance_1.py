class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodicals(Publication):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodicals):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)

class Newspaper(Periodicals):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)


b1 = Book("Catch 22", "Joseph Heller", 345, 499.99)
m1 = Magazine("India Today", "Weekly", 7, 10.0)
n1 = Newspaper("The Hindu", "Amrit Bazar Patrika", 15, 30.0)