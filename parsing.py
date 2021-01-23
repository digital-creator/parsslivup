from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
from func.request import find_element, results_count, parse_page, page_next
from func.write_data import write_file

def parsing(link, wait, search, rows):
    options = Options()
    options.headless = True
    with webdriver.Firefox(timeout=15, options = options) as driver:
        driver.implicitly_wait(wait)
        driver.get(link)
        sleep(wait)
        element = find_element(driver)
        element.send_keys(f'{search}')
        element.submit()
        sleep(wait)
        try:
            res_count = results_count(driver)
        except Exception as e:
            print(f'Исключение: {e}\n'
                  f'Типа {type(e)}\n'
                  f'Поиск не дал результатов')
        print(f'Найдено {res_count} страниц\n')
        count_page = int(input('Сколько страниц будем парсить?'))
        try:
            if count_page > 1:
                for page in range(1, count_page + 1):
                    if page == 1:
                        data = parse_page(driver, rows)
                        write_file(search, data)
                        page_next(driver, page + 1)
                    else:
                        data = parse_page(driver, rows)
                        write_file(search, data)
                        page_next(driver, page + 1)
            else:
                data = parse_page(driver, rows)
                write_file(search, data)
        except Exception as excpt:
            print(f'Возникло исключение {excpt}\n'
                  f'Исключение типа: {type(excpt)}\n'
                  f'На странице оказалось меньше {rows} элементов')
            quit()
