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

        def popularity(self) -> str:
            """
            Функкция, которая проверяет, популярна ли Социальная сеть. Если количество
            пользователей превышает 1000000, то популярна.
            """
            if self.users > 1000000:
                return "Данная социальная сеть популярна"
            else:
                return "Данная социальная сеть не популярна"

        def advertising(self) -> int:
            """
            Функкция, которая возвращает приблезительное количество рекламных постов,
            в зависимости от количества пользователей.
            """
            ...

        def __str__(self) -> str:
            return f"Социальная сеть имеет следующее количество пользователей: {self.users}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}users={self.users!r})"


    class Vk(SocialMedia):
        def __init__(self, users: int, group_amount: int):
            """
            Создание и подготовка к работе объекта "Социальная сеть Vk"
            Класс "Vk"- дочерний класс от "SocialMedia"

            :param users: Количество пользователей
            :param group_amount: Количество сообществ Вконтакте
            """
            super().__init__(users)
            super().popularity()
            self.group_amount = group_amount

        def advertising(self) -> int:
            """
            Функкция, которая оценивает приблезительное количество рекламных постов,
            в зависимости от количества пользователей.

            Функция перегружена, поскольку в каждой социальной сети свои правила
            публикации рекламных постов.
            """
            ...

        def __str__(self) -> str:
            return f"Количество пользователей Vk: {self.users}. Количество сообществ Вконтакте: {self.group_amount}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(users={self.users!r}, group_amount={self.group_amount!r})"

    social_media1 = Vk(1000000000, 5)
    print(social_media1.popularity())

    pass
