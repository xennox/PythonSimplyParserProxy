import requests
import colorama # Чтобы было прикольней и весело
from colorama import Fore
colorama.init()
from bs4 import BeautifulSoup

max_page = 5        # я пытался. а потом подумал что лучше не буду возится с файлами, оставил это тут для ознакомления
pages =[]



def get_html(url):          # Запрос через цикл - для слабаков!!!
    r = requests.get(url)
    return r.text

def get_html2(url2):        # Запрос через цикл - для слабаков!!!
    r = requests.get(url2)
    return r.text

def get_html3(url3):        # Запрос через цикл - для слабаков!!!
    r = requests.get(url3)
    return r.text

def get_html4(url4):        # Запрос через цикл - для слабаков!!!
    r = requests.get(url4)
    return r.text

def get_html5(url5):        # Запрос через цикл - для слабаков!!!
    r = requests.get(url5)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')  # Подрубаем парсер lxml из супа для парсинга и запихиваем все что врубили в переменную
    line = soup.find('table', id='theProxyList').find('tbody').find_all('tr') # указываем супу, в котором мы все врубили, что ему выбрать для нас и
                                                                                # помещаем это в переменную которая как строка-линия

    file = open("proxy.txt", "a")                                               # Создаем файл для дозаписи СРАЗУ
    file.close()                                                                # Закрываем файл, чтобы не создавать снова. а дозаписывать его в цикле НА ВСЯКИЙ СЛУЧАЙ

    for tr in line:                                                             # пока у нас есть tr в линии которую мы указали супу как строку
        td = tr.find_all('td')                                                  # ищем td
        ip = td[1].text                                                         # эти td помешаем в переменную IP
        port = td[2].text                                                       # а эти td в переменную port

        print(Fore.RED + ip + ":" + Fore.GREEN + port)                          # вывод в консоль через разделитель двоеточие
        file = open("proxy.txt", "a")                                           # попытки весь вывод автоматически запихнуть в txt, ато не круто
        file.write(str(ip + ":" + port + '\n'))                                 # попытки весь вывод автоматически запихнуть в txt, ато не круто
    file.close()

def main():
    url = 'http://foxtools.ru/Proxy'        # Массивы ссылок - для слабаков!!!
    url2 = 'http://foxtools.ru/Proxy?page=2'# Массивы ссылок - для слабаков!!!
    url3 = 'http://foxtools.ru/Proxy?page=3'# Массивы ссылок - для слабаков!!!
    url4 = 'http://foxtools.ru/Proxy?page=4'# Массивы ссылок - для слабаков!!!
    url5 = 'http://foxtools.ru/Proxy?page=5'# Массивы ссылок - для слабаков!!!
    get_page_data(get_html(url))            # Массивы ссылок - для слабаков!!!
    get_page_data(get_html2(url2))          # Массивы ссылок - для слабаков!!!
    get_page_data(get_html3(url3))          # Массивы ссылок - для слабаков!!!
    get_page_data(get_html4(url4))          # Массивы ссылок - для слабаков!!!
    get_page_data(get_html5(url5))          # Массивы ссылок - для слабаков!!!


if __name__ == '__main__':                  # конструктор
    main()
