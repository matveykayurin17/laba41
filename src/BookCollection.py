import logging
from src.Book1 import Book
from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger=logging.getLogger(__name__)

class BookCollection:
    def __init__(self):
        """При помощи конструкторе создаётся список и поле"""
        self.lst=[]
        self.index=0

    def add(self,name:Book)->None:
        """Функция добавляет name в список"""
        self.lst.append(name)

    def remove(self,name:Book)->None:
        """Функция удаляет name из списка"""
        if name in self.lst:
            self.lst.remove(name)


    def __len__(self):
        """Функция возвращает длину списка"""
        return len(self.lst)

    def __iter__(self):
        """Функция вместе с функцией next позволяет итерироваться по списку"""
        return self

    def __next__(self):
        """Функция вместе с функцией iter позволяет итерироваться по списку"""
        if self.index<len(self.lst):
            result=self.lst[self.index]
            self.index+=1
            return result
        else:
            raise StopIteration

    def __str__(self):
        """Функция нужна для вывода содержимое коллекции на экран в нужном виде"""
        special_string="["
        for item1 in self.lst:
            if item1!=self.lst[-1]:
                special_string += str(item1)
                special_string += ","
                special_string += " "
            else:
                special_string+=str(item1)
                special_string+="]"
        return special_string

    def __getitem__(self, item: int | slice):
        """Функция позволяет получить элемент по индексу/срезу"""
        try:
            if isinstance(item,slice):
                start=item.start
                stop=item.stop
                step=item.step
                return self.lst[start:stop:step]
            elif isinstance(item,int):
                return self.lst[item]
            else:
                return "Индекс должен быть целым числом"
        except IndexError as e:
            logger.error(f"Ошибка:{e}")

    def __contains__(self, item:Book):
        """Функция позволяет определить есть ли в списке элемент или нет"""
        return item in self.lst