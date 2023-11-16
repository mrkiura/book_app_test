from models import Book
from typing import Union


class BookStorage:
    _id = 0

    def __init__(self) -> None:
        self._books = []

    def all(self):
        return [book._asdict() for book in self._books]

    def get(self, id: int) -> Union[Book, None]:
        for book in self._books:
            if book.id == id:
                return book

        return None

    def create(self, **kwargs) -> Book:
        self._id += 1
        kwargs["id"] = self._id
        book = Book(**kwargs)
        self._books.append(book)
        return book

    def delete(self, id) -> None:
        for index, book in enumerate(self._books):
            if book.id == id:
                del self._books[index]
