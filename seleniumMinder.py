## Обозначение библиотек
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from random import randint

## Обозначение переменных
debugpref = 'Debug: '  # Префикс для Debug вывода
chosen = ''  # Будущий выбранный url из списка urls
newurl = '' # Будущий добавленный пользователем url

## Обозначение драйвера хрома и его настроек
driver = webdriver.Chrome()
options = ChromeOptions()

## Список url сайтов на случайный выбор
urls = [
    'https://youtube.com',
    'https://facebook.com',
    'https://roblox.com',
]

## Обозначение функций за __init__
def driveOpen(url):
    try:
        print('Попытка открытия новой сессии браузера..')
        driver.get(url)
    except Exception as error:
        print(f'{debugpref}что-то не так! Ошибка: {error}')
def PickUrl(newurl):
    try:
        if len(urls) == 0:
            newurl = input('Введите url для запуска. Пример: https://google.com или http://вашдомен.хх')
        def newurladd():
            newurl = input('При необходимости введите url тут или в списке urls. Пример: https://google.com или http://вашдомен.хх . Для отмены нажмите Enter.')
            if newurl != '':
                urls.append(newurl)
                print(f'{debugpref}Программа завeршена! Не было введено ни одного url.')
                quit()
                print(f'{debugpref}Url добавлен!')
                newurladd()
            elif len(urls) == 0:
                quit()
            elif newurl == '':
                chosen = urls[randint(0, len(urls) - 1)]
                print(chosen)
                driveOpen(chosen)
        newurladd()
    except Exception as error:
        print(f'{debugpref}что-то не так! Ошибка: {error}')

## __init__ запуск цикла
def __init__():
    if __name__ == '__main__':
        PickUrl(newurl)

__init__()