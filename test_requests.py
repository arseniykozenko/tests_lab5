"""Тесты для REST API запросов"""
import requests

BASE_URL = "https://reqres.in/api"
TIMEOUT = 10
HEADERS = {"Content-Type": "application/json", "x-api-key": "reqres-free-v1"}

class TestRequests:
    """Тесты для REST API запросов"""
    def test_get_user(self):
        """Тестирование получения данных о пользователе"""
        response = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT, headers=HEADERS)
        assert response.status_code == 200, 'Неверный код ответа!'

        data = response.json()
        assert 'data' in data, 'Нет данных в ответе'
        assert all(key in data['data'] for key in \
                   ['id', 'email', 'first_name', 'last_name', 'avatar']), \
                        'Нет необходимых полей в ответе'
        assert data['data']['id'] == 1, 'Неверный id!'
        assert '@' in data['data']['email'], 'Неверный email!'

    def test_create_user(self):
        """Тестирование создания пользователя"""
        payload = {
            "name": "Ivan Ivanov",
            "age": 22,
            "job": "Backend Developer"
        }
        response = requests.post(f"{BASE_URL}/users", json=payload, timeout=TIMEOUT, headers=HEADERS)
        assert response.status_code == 201, 'Неверный код ответа!'

        data = response.json()
        assert all(key in data for key in \
                   ['name', 'age', 'job', 'id', 'createdAt']), \
                        'Нет необходимых полей в ответе'
        assert data['name'] == "Ivan Ivanov", 'Неверное имя'
        assert data['job'] == "Backend Developer", 'Неверная работа'
        assert data['age'] == 22, 'Неверный возраст'

    def test_update_user(self):
        """Тестирование обновления пользователя"""
        payload = {
            "name": "Dmitrii Ivanov",
            "age": 21,
            "job": "Frontend Developer"
        }
        response = requests.put(f"{BASE_URL}/users/2", json=payload, timeout=TIMEOUT, headers=HEADERS)
        assert response.status_code == 200, 'Неверный код ответа'

        data = response.json()
        assert all(key in data for key in \
                   ['name', 'age', 'job', 'updatedAt']), \
                        'Нет необходимых полей в ответе'
        assert data['name'] == "Dmitrii Ivanov", 'Неверное имя'
        assert data['job'] == "Frontend Developer", 'Неверная работа'
        assert data['age'] == 21, 'Неверный возраст'
