from typing import List
from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        self.library.add_book(Book(title, author, year))

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        for book in self.library.get_books():
            # Вважаю використання logger тут недоречним
            # так як ми працюємо з виводом даних, а не їх логуванням.
            # Також в моєму випадку використання logger призводило
            # до проблем з відображенням наступних команд.
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")


# Клас Library лише виконує функції колекції книг
# Розширення або заміна його реалізації ніяк не вплине
# на створення нових обєктів книг та виведення інформації про них
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def get_books(self):
        return self.books


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
