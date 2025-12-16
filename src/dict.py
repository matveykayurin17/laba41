import abc
import logging
from src.Book1 import Book
from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger=logging.getLogger(__name__)

class IndexDict:
    dictionary:dict
    def __init__(self):
        """В конструкторе создаётся словарь и поле"""
        self.dictionary={}
        self.index=0

    def __len__(self):
        """Функция возвращает длину словаря"""
        return len(self.dictionary)

    def __getitem__(self, item:Book):
        """Функция возвращает значение по ключу"""
        try:
            return self.dictionary[item]
        except KeyError as e:
            logger.error(f"Ошибка:{e}")

    def __iter__(self):
        """Функция вместе с функцией next позволяет итерироваться по словарю"""
        return self

    def __next__(self):
        """Функция вместе с функцией iter позволяет итерироваться по словарю"""
        if self.index < len(self.dictionary):
            result = [list(self.dictionary.keys())[self.index]]
            self.index += 1
            return result
        else:
            raise StopIteration

    @abc.abstractmethod
    def append_key_value(self,book:Book):
        """Создал функцию, которую потом буду переопределять в классах наследниках"""
        pass

    @abc.abstractmethod
    def remove_key_value(self, key1:int | str)->None:
        pass

    def index1(self,key1)->Book:
        try:
            special_string="["
            count=0
            for item in self.dictionary[key1]:
                if count!=len(self.dictionary[key1])-1:
                    special_string+=str(item)
                    special_string+=","
                    special_string+=" "
                else:
                    special_string+=str(item)
                    special_string+="]"
                count+=1
            return special_string
        except KeyError as e:
            logger.error(f"Ошибка {e}")

    def __str__(self):
        """Функция нужна для вывода содержимое коллекции на экран в нужном виде"""
        special_string="["
        count=0
        for item1 in self.dictionary.keys():
            if count!=len(self.dictionary)-1:
                special_string += str(item1)
                special_string += ","
                special_string += " "
            else:
                special_string+=str(item1)
                special_string+="]"
            count+=1
        return special_string


class YearDict(IndexDict):
    def append_key_value(self,book:Book)->None:
        """Функция добавляет значение если ключ уже существует, или добавляет пару ключ значение если такого ключа ещё нет"""
        try:
            list2 = self.dictionary[book.year]
            list2.append(book)
            self.dictionary[book.year] = list2
        except KeyError:
            self.dictionary[book.year] = [book]

    def remove_key_value(self, book: Book) ->None:
        try:
            """Функция удаляет ключ и значение"""
            list3 = self.dictionary[book.year]
            list3.remove(book)
            self.dictionary[book.year] = list3
        except KeyError as e:
            logger.error(f"ошибка:{e}")


class AuthorDict(IndexDict):
    def append_key_value(self, book: Book)->None:
        """Функция добавляет значение если ключ уже существует, или добавляет пару ключ значение если такого ключа ещё нет"""
        try:
            list4 = self.dictionary[book.author]
            list4.append(book)
            self.dictionary[book.author] = list4
        except KeyError:
            self.dictionary[book.author] = [book]

    def remove_key_value(self, book: Book) ->None:
        try:
            """Функция удаляет ключ и значение"""
            list5 = self.dictionary[book.author]
            list5.remove(book)
            self.dictionary[book.author] = list5
        except KeyError as e:
            logger.error(f"ошибка:{e}")

class IsbnDict(IndexDict):
    def append_key_value(self,book:Book)->None:
        """Функция добавляет значение если ключ уже существует, или добавляет пару ключ значение если такого ключа ещё нет"""
        self.dictionary[book.isbn]=book

    def remove_key_value(self, book: Book) ->None:
        try:
            """Функция удаляет ключ и значение"""
            del self.dictionary[book.isbn]
        except KeyError as e:
            logger.error(f"ошибка:{e}")

    def index1(self,key1)->Book:
        try:
            return self.dictionary[key1]
        except KeyError as e:
            logger.error(f"Ошибка {e}")