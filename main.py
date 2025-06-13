import requests

# Функция для поиска скрытых директорий
def find_hidden_directories(base_url, wordlist_file):
    try:
        # Открываем файл со списком имен директорий
        with open(wordlist_file, 'r') as file:
            directories = file.read().splitlines()

        print(f"Начинаем поиск скрытых директорий на {base_url}\n")

        # Перебираем каждую директорию из списка
        for directory in directories:
            url = f"{base_url}/{directory}"  # Формируем полный URL
            response = requests.get(url)

            # Проверяем код ответа
            if response.status_code == 200:
                print(f"[+] Найдена директория: {url}")
            elif response.status_code == 403:
                print(f"[-] Доступ запрещен: {url}")
            elif response.status_code == 404:
                pass  # Пропускаем несуществующие директории
            else:
                print(f"[?] Неизвестный статус ({response.status_code}): {url}")

    except FileNotFoundError:
        print("Ошибка: Файл wordlist не найден.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")

# Основная часть программы
if __name__ == "__main__":
    # Введите базовый URL сайта
    base_url = "сайт"

    # Укажите путь к файлу со списком имен директорий
    wordlist_file = "файл.txt"

    # Запускаем поиск
    find_hidden_directories(base_url, wordlist_file)