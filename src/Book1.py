class Book:
    title:str
    author:str
    year:int
    genre:str
    isbn:int

    def __init__(self,title,author,year,genre,isbn):
        self.title=title
        self.author=author
        self.year=year
        self.genre=genre
        self.isbn=isbn

    def __str__(self):
        return self.title+","+" "+self.author+","+" "+str(self.year)+","+" "+self.genre+","+" "+str(self.isbn)