from unicodedata import name

class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        self.chapters = []

    def addChapter(self, chapter):
        self.chapters.append(chapter)

    def getBookPageCount(self):
        result =0
        for ch in self.chapters:
            result+= ch.pagecount
        return result
    
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pagecount = pages

leo = Author("Leo", "Tolstoy") 
b1 = Book("War and Peace", 199, leo)
c1 = Chapter("Introduction", 39 )

b1.addChapter(c1)
print(b1.getBookPageCount())    
