class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret="this cannot be accessed"

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


b1 = Book("Catch 22", "Joseph Heller", 345, 499.99)
b1.showDetails()
b1.setDiscount(0.15)
b1.showDetails()

print(dir(b1))
print("__secret cannot be accessed as it is, there is a way to access it")
print("Example of name mangling:")
print(b1._Book__secret)

