class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


class Magazine:
    def __init__(self, title, publisher, period, price):
        self.title = title
        self.publisher = publisher
        self.period = period
        self.price = price

class Newspaper:
    def __init__(self, title, publisher, period, price):
        self.title = title
        self.publisher = publisher
        self.period = period
        self.price = price

b1 = Book("Catch 22", "Joseph Heller", 345, 499.99)
m1 = Magazine("India Today", "Weekly", 7, 10.0)
n1 = Newspaper("The Hindu", "Amrit Bazar Patrika", 15, 30.0)