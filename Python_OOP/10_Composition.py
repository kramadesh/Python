class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price
        self.authorfname = authorfname
        self.authorlname = authorlname
        self.chapters = []

    def addChapter(self, name, pages):
        self.chapters.append(name, pages)

    