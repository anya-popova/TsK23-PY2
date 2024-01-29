class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name  # внутри класса обращаемся к защищенному атрибуту

    @property
    def author(self):
        return self._author  # внутри класса обращаемся к защищенному атрибуту

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages <= 0:
            raise ValueError
        self._pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    """ Класс аудио книги. """
    def __init__(self, name: str, author: str, duration: int):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: int) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if duration <= 0:
            raise ValueError
        self._duration = duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
