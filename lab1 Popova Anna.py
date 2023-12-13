import doctest
from typing import Union


class Table:
    def __init__(self, height: Union[int, float], material: str):
        """
        Создание и подготовка к работе объекта "Стол"

        :param height: Высота стола
        :param material: Материал, из которого изготовлен стол

        Примеры:
        >>> table = Table(150.1, "Дерево")  # инициализация экземпляра класса
        """
        self.height = None
        self.height_real(height)
        self.material = material

    def height_real(self, height: float):
        """
        Функкция, которая проверяет, реальная ли высота стола введена
        :param height: Высота стола

        :raise TypeError: Если высота стола не int или float, то вызываем ошибку
        :raise ValueError: Если стол заданной высоты существовать не может, вызываем ошибку

        Пример:
        >>> table = Table(150.1, "Дерево")
        >>> table.height_real(150.1)
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if not height > 0:
            raise ValueError("Высота тола должна быть больше 0")
        self.height = height

    def material_density(self, material: str):
        """
        Функкция, которая определяет плотность материала
        :param material: Материал, из которого изготовлен стол

        Пример:
        >>> table = Table(150.1, "Дерево")
        >>> table.height_real(150.1)
        """
        ...


class User:
    def __init__(self, nickname: str, age: int):
        """
        Создание и подготовка к работе объекта "Пользователь"

        :param nickname: Никнейм пользователя
        :param age: Возраст пользователя

        Примеры:
        >>> user = User("Nick", 17)  # инициализация экземпляра класса
        """
        self.nickname = nickname
        self.age = None
        self.age_real(age)

    def age_real(self, age: int):
        """
        Функкция, которая проверяет, реальный ли возраст введён
        :param age: Введённый возраст пользователя

        :raise ValueError: Если возраст введён неверно, то вызываем ошибку

        Пример:
        >>> user = User("Nick", 17)
        >>> user.age_real(17)
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        self.age = age

    def age_category(self, age: int):
        """
        Функкция, которая определяет возрастную категорию пользователя
        :param age: Введённый возраст пользователя

        Пример:
        >>> user = User("Nick", 17)
        >>> user.age_category(17)
        """
        ...


class Magazine:
    def __init__(self, season: int, pages: int):
        """
        Создание и подготовка к работе объекта "Журнал"

        :param season: Номер сезона, по которому выпущен журнал
        :param pages: Количество страниц журнала

        Примеры:
        >>> magazine = Magazine(4, 21)  # инициализация экземпляра класса
        """
        self.season = None
        self.init_season(season)
        self.pages = None
        self.init_pages(pages)

    def init_season(self, season: int):
        """
        Функкция, которая проверяет, существующий ли номер сезона введён
        :param season: Номер сезона

        Пример:
        >>> magazine = Magazine(4, 21)
        >>> magazine.init_season(4)
        """
        ...

    def init_pages(self, pages: int):
        """
        Функкция, которая проверяет, верно ли введено количество страниц
        :param pages: Количество страниц в журнале

        Пример:
        >>> magazine = Magazine(4, 21)
        >>> magazine.init_pages(21)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
