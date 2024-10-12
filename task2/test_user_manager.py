from user_manager import UserManager

def test_user_manager():
    user_manager = UserManager()

    # Тестирование добавления пользователей
    print("Тестирование добавления пользователей...")
    user_manager.add_user("alice", "alice@example.com")
    assert user_manager.user_exists("alice") is True, "Ошибка: Пользователь 'alice' должен существовать."

    try:
        user_manager.add_user("alice", "alice_new@example.com")
    except ValueError as e:
        assert str(e) == "Пользователь с таким именем уже существует.", "Ошибка: Должно быть выброшено исключение."

    # Тестирование получения информации о пользователе
    print("Тестирование получения информации о пользователе...")
    assert user_manager.get_user("alice") == "alice@example.com", "Ошибка: Неверный email для 'alice'."

    # Тестирование удаления пользователя
    print("Тестирование удаления пользователя...")
    user_manager.remove_user("alice")
    assert user_manager.user_exists("alice") is False, "Ошибка: Пользователь 'alice' не должен существовать."

    try:
        user_manager.get_user("alice")
    except ValueError as e:
        assert str(e) == "Пользователь не найден.", "Ошибка: Должно быть выброшено исключение."

    # Тестирование удаления несуществующего пользователя
    print("Тестирование удаления несуществующего пользователя...")
    try:
        user_manager.remove_user("bob")
    except ValueError as e:
        assert str(e) == "Пользователь не найден.", "Ошибка: Должно быть выброшено исключение."

    print("Все тесты пройдены успешно!")


# Запуск тестов
if __name__ == "__main__":
    test_user_manager()