class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        
    def getPrice(self):
        if hasattr(self, "_discount"):
            price = self.price-(self.price*self._discount)
        else:
            price = self.price
        return float("{:.2f}".format(price))
    
    def setDiscount(self, discount):
        self._discount = discount

    def showDetails(self):
        print(f"\
        Name:            {self.title}, \n\
        Written By:      {self.author},\n\
        Number of pages: {self.pages},\n\
        Price:           {self.getPrice()} \n")


class Magazine:
    def __init__(self, title, frequency, price):
        self.title = title
        self.frequency = frequency
        self.price  = price



b1 = Book("Catch 22", "Joseph Heller", 345, 499.99)
b1.showDetails()

m1 = Magazine("India Today", "Weekly", 10.0)
print(type(b1))
print(type(m1))
print(isinstance(b1, Book))
print(isinstance(m1, Book))

