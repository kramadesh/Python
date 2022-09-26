class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        
    __booklist = None

    def getPrice(self):
        if hasattr(self, "_discount"):
            price = self.price-(self.price*self._discount)
        else:
            price = self.price
        return float("{:.2f}".format(price))
    
    def setDiscount(self, discount):
        self._discount = discount

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def showDetails(self):
        print(f"\
        Name:            {self.title}, \n\
        Written By:      {self.author},\n\
        Number of pages: {self.pages},\n\
        Price:           {self.getPrice()} \n")


b1 = Book("Catch 22", "Joseph Heller", 345, 499.99)
b1.showDetails()

b2 = Book("The Hitchhiker's guide to Galaxy", "Christopher Hitchens", 350, 599.95)

books = Book.getbooklist()
books.append(b1)
books.append(b2)
print(books)

