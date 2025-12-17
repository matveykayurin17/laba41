import pytest
from src.BookCollection import BookCollection
from src.dict import YearDict,IsbnDict,AuthorDict
from src.Book1 import Book

class Test:
    def tests(self):
        book1=Book("Красная шапочка","Не понмю",2025,"drama",123)
        book2 = Book("Красная шапочка1", "Не понмю1", 20251, "drama1", 1231)
        book3 = Book("Красная шапочка2", "Не понмю2", 20252, "drama2", 1232)
        test_book=BookCollection()
        test_book.add(book1)
        test_book.add(book2)
        test_book.add(book3)
        test_book.remove(book3)
        assert test_book.__len__()==2
        assert test_book.__getitem__(0)==book1
        assert test_book.__contains__(book1)  is True

    def tests1(self):
        book4 = Book("m", "m1", 2, "m2", 4)
        book5 = Book("m4", "m5", 3, "m6", 5)
        book6 = Book("m7", "m8", 4, "m9", 6)

        test2_book = YearDict()
        test3_book = AuthorDict()
        test4_book = IsbnDict()

        test2_book.append_key_value(book4)
        test2_book.append_key_value(book5)
        test2_book.append_key_value(book6)

        test3_book.append_key_value(book4)
        test3_book.append_key_value(book5)
        test3_book.append_key_value(book6)


        test4_book.append_key_value(book4)
        test4_book.append_key_value(book5)
        test4_book.append_key_value(book6)


        test3_book.remove_key_value(book6)
        test4_book.remove_key_value(book6)
        test2_book.remove_key_value(book6)


        assert test4_book.__len__()==2
        assert test3_book.__len__()==2
        assert test2_book.__len__()==2
