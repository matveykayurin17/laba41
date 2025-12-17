from src.BookCollection import BookCollection
from src.dict import YearDict, IsbnDict, AuthorDict
from src.Book1 import Book


class Library:
    list1: BookCollection
    dict1: YearDict
    dict2: IsbnDict
    dict3: AuthorDict

    def __init__(self):
        """Конструктор в котором создаются объекты класса"""
        self.list1 = BookCollection()
        self.dict1 = YearDict()
        self.dict2 = IsbnDict()
        self.dict3 = AuthorDict()

    def add1(self, name: Book)->None:
        """Функция для добавления элемента в коллекцию"""
        self.list1.add(name)
        self.dict1.append_key_value(name)
        self.dict2.append_key_value(name)
        self.dict3.append_key_value(name)

    def remove1(self, name: Book)->None:
        """Функция для удаления элемента из коллекции"""
        self.list1.remove(name)
        self.dict1.remove_key_value(name)
        self.dict2.remove_key_value(name)
        self.dict3.remove_key_value(name)

    def __str__(self):
        """Функция прописана для возможности выводить содержимое библиотеки"""
        self.list1.__str__()
        self.dict1.__str__()
        self.dict2.__str__()
        self.dict3.__str__()

    def search(self, isbn:int):
        """Функция для поиска значения по isbn"""
        return self.dict2.index1(isbn)

    def search2(self, year:int):
        """Функция для поиска значения по году"""
        return self.dict1.index1(year)

    def search3(self, author:str):
        """Функция для поиска значения по автору"""
        return self.dict3.index1(author)
