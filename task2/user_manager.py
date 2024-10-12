class UserManager:
    def __init__(self):
        """Инициализация пустого списка пользователей."""
        self.users = {}  # Словарь для хранения пользователей в формате {имя: email}

    def add_user(self, username: str, email: str) -> None:
        """Добавляет нового пользователя с уникальным именем."""
        if username in self.users:
            raise ValueError("Пользователь с таким именем уже существует.")
        self.users[username] = email

    def remove_user(self, username: str) -> None:
        """Удаляет пользователя по имени."""
        if username not in self.users:
            raise ValueError("Пользователь не найден.")
        del self.users[username]

    def get_user(self, username: str) -> str:
        """Возвращает email пользователя по имени."""
        if username not in self.users:
            raise ValueError("Пользователь не найден.")
        return self.users[username]

    def user_exists(self, username: str) -> bool:
        """Проверяет, существует ли пользователь."""
        return username in self.users


if __name__ == "__main__":
    user_manager = UserManager()
    user_manager.add_user("ali", "ali@example.ru")
    print(user_manager.get_user("ali"))  # Вывод: alice@example.com
