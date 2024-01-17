from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class PressFormatter:
    @staticmethod
    def format(book: Book):
        return book.content[:20]


class EmailFormatter:
    @staticmethod
    def format(book: Book):
        return book.content[:50]


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter):
        formatted_book = formatter.format(book)
        return formatted_book
