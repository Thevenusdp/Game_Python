# Импорт пакета
import random, time, os

# Очистить экран (кроссплатформенный, смешной)
def clear_screen():
    # Не учитесь так писать, я экономлю время
    if os.sep == '/':
        os.system('clear')
    else:
        os.system('cls')

# Аналоговый эффект задержки
def delay_waiting(content, frequency):
    print('%s.' % content, end='', flush=True)
    for x in range(1, frequency):
       time.sleep(1)
       print('.', end='', flush=True)
    time.sleep(1)
    print(' succeeded.')

# Имитация посадки Сиона хозяином
def login_zion():
    clear_screen()
    delay_waiting('connecting to Zion host', 2)
    time.sleep(0.5)
    print('enter username: Neo')
    time.sleep(0.2)
    print('enter password: ******')
    time.sleep(0.2)
    delay_waiting('logging in.', 2)
    time.sleep(0.7)
    clear_screen()
    print('Hello, Neo.')
    time.sleep(1)

# Имитация посадки Сиона хозяином
login_zion()
# Очистить экран
clear_screen()
# Создайте набор символов, содержащий a-z, A-Z, 0-9
charts = [*[chr(x) for x in range(65, 123) if x not in range(91, 97)], *map(str, range(10))]
# Бесконечный цикл
while True:
    # Каждая задержка печати составляет 0,009 секунды
    time.sleep(0.009)
    # Максимальное количество символов на моем экране - 158
    # 79 здесь для отображения, между каждым символом будет пробел, а затем ровно 158 символов (78 символов + 78 пробелов + 1 символ)
    # Или вы также можете написать:
    #     print((' ' * 3).join(random.choices(charts, k=40)))
    print(*random.choices(charts, k=79))

