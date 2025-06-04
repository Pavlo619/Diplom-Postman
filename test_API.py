import requests
import allure


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36","authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIyMDYwODYwLCJpYXQiOjE3NDkwNjIwNjMsImV4cCI6MTc0OTA2NTY2MywidHlwZSI6MjB9.wUsxvp85D9ryit88DcEl6igEr2CjJbHbIVUgI74Ycc4"}
base_url = "https://web-gate.chitai-gorod.ru/api/v2/"


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=джоан роулинг", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по названию")
@allure.description("Проверка, что API возвращает книгу с ожидаемым названием")
def test_api_book_by_title():
    resp = requests.get(f"{base_url}search/product?phrase=капитанская дочка", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска книги по автору на английском")
@allure.description("Проверка, что API возвращает книгу с ожидаемым названием на английском.")
def test_search_by_language_english():
    resp = requests.get(f"{base_url}search/product?phrase=The lord of rings", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с недопустимой японской фразой")
@allure.description("Проверка, что API возвращает ошибку при поиске с недопустимой японской фразой.")
def test_negative_api_Japanese():
    resp = requests.get(f"{base_url}search/product?phrase=人で座ってください", headers=headers)
    assert resp.status_code == 422

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Тестирование поиска с пустым запросом")
@allure.description("Проверка, что API возвращает ошибку при пустом поисковом запросе.")
def test_negative_api_empty_search():
    resp = requests.get(f"{base_url}search/product?phrase=", headers=headers)
    assert resp.status_code == 400