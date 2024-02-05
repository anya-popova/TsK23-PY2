import doctest


if __name__ == "__main__":
    # Write your solution here
    class SocialMedia:
        def __init__(self, users: int):
            """
            Создание и подготовка к работе объекта "Социальная сеть"

            :param users: Количество пользователей

            Примеры:
            # >>> social_media = SocialMedia(150000)  # инициализация экземпляра класса
            """
            self.users = users

        def popularity(self) -> int:
            """
            Функкция, которая проверяет, популярна ли Социальная сеть. Если количество
            пользователей больше 1000000, то популярна, возвращается 1; иначе 0
            """
            if self.users > 1000000:
                return 1
            else:
                return 0

        def __str__(self) -> str:
            return f"Социальная сеть имеет следующее количество пользователей: {self.users}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}users={self.users!r})"


    class Vk(SocialMedia):
        def __init__(self, users: int, advertising_amount: int):
            """
            Создание и подготовка к работе объекта "Социальная сеть Vk"
            Класс "Vk"- дочерний класс от "SocialMedia"

            :param users: Количество пользователей
            :param advertising_amount: Количество рекламных постов
            """
            super().__init__(users)
            super().popularity()
            self.advertising_amount = advertising_amount

        def __str__(self) -> str:
            return f"Количество пользователей Vk: {self.users}. Количество рекламных постов: {self.advertising_amount}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(users={self.users!r}, advertising_amount={self.advertising_amount!r})"


    pass
