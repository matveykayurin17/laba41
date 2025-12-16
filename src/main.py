import random
import logging
from src.Library import Library
from src.Book1 import Book
from src.constants import title1,author1,year1,genre1
from src.config import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)
logger=logging.getLogger(__name__)





class Main:
    isbn=0
    library1: Library
    book1:Book=['1','2',0,'3',121331221]
    @staticmethod
    def main(steps: int = 100, seed: int | None = None) -> None:
        Main.library1=Library()
        Main.run_simulation(Main(),steps,seed)


        """
        Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
        :return: Данная функция ничего не возвращает
        """
    def run_simulation(self,steps: int = 20, seed: int | None = None) -> None:
        if seed is None:
            for i in range(steps):
                random1 = random.randint(0, 3)
                if random1 == 0:
                    self.add_book()
                elif random1 == 1:
                    self.random_delete()
                elif random1 == 2:
                    self.search()
                else:
                    self.notsearch()
        else:
            random.seed(seed)

    def add_book(self):
        title=title1[random.randint(0,len(title1)-1)]
        author=author1[random.randint(0,len(author1)-1)]
        year=year1[random.randint(0,len(year1)-1)]
        genre=genre1[random.randint(0,len(genre1)-1)]
        new=Book(title, author, year, genre, self.isbn)
        logger.info("Добавлена новая книга")
        self.library1.add1(new)
        self.isbn+=1

    def random_delete(self):
        if len(self.library1.list1)>=1:
            delete1: Book = self.library1.list1[random.randint(0, len(self.library1.list1) - 1)]
            logger.info("Книга удалена")
            self.library1.remove1(delete1)
        else:
            logger.info("Список книг пуст")

    def search(self):
        if len(self.library1.list1)>=1:
            random1=random.randint(0,2)
            book=self.library1.list1[random.randint(0,len(self.library1.list1)-1)]
            if random1==0:
                logger.info(self.library1.search(book.isbn))
            elif random==1:
                logger.info(self.library1.search2(book.year))
            else:
                logger.info(self.library1.search3(book.author))
        else:
            logger.info("Список книг пуст")


    def notsearch(self):
        random1=random.randint(0,2)
        if not self.library1.list1.__contains__(self.book1):
            if random1 == 0:
                try:
                    logger.info(self.library1.search(self.book1.isbn))
                except Exception:
                    logger.error("Такой книги не существует")
            elif random1 == 1:
                try:
                    logger.info(self.library1.search2(self.book1.year))
                except Exception:
                    logger.error("Такой книги не существует")
            else:
                try:
                    logger.info(self.library1.search3(self.book1.author))
                except Exception:
                    logger.error("Такой книги не существует")
        else:
            logger.info("Поищите книгу получше")
if __name__=="__main__":
    Main.main()








