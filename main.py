from threading import Thread
from parsing import parsing


link = 'https://slivup.us'

try:
    wait = int(input('Укажите задержу'))
except Exception as e:
    print(f'Исключение: {e}', f'Тип исключения {type(e)}', sep='\n')
    print('Вы не указали задержку\n'
          'Выбрано значение по-умолчанию: 15 секунд')
    wait = 5

try:
    flag = True
    while flag == True:
        search = str(input('По каким ключевым словам будем парсить slivup?\n'
                           'Если несколько объектов, то укажите их через пробел\n')).lower()
        try:
            if ' ' in search:
                search = search.split(' ')
                for i in range(0, len(search) + 1):
                    if len(search[i]) <= 2:
                        print('Ключевое слово должно состоять из более, чем 2-х символов', end = '\n')
                        print(search[i])
                        break
                    else:
                        flag = False
                        flag_thread = int(input('Выбрано несколько ключевых слов для парсинга\n'
                                                'Воспользуемся парсингом в несколько потоков?\n'
                                                '1 - Да\n'
                                                '0 - Нет\n'))
                        if flag_thread == 1:
                            thread = True
                            break
                        else:
                            thread = False
                            break

            elif len(search) <= 2:
                print('Ключевое слово должно состоять из более, чем 2-х символов', end='\n')
            else:
                flag = False
                thread = False
        except IndexError as ve:
            print('Вы не ввели ни одного ключевого слова')
except Exception as e:
    print('Введите ключевые слова через пробел', type(e))

try:
    rows = int(input('Введите количество строк на странице'))
except Exception as e:
    print(f'Исключение: {e}', f'Тип исключения {type(e)}', sep = '\n')
    print('Вы не указали количество строк на странице\n'
          'Выставлено значение по-умолчанию: 25')
    rows = 25



if __name__ == '__main__':
    try:
        if thread == True:
            threads = list()
            for index in range(len(search)):
                x = Thread(target=parsing(link, wait, search[index], rows), args=(index,))
                threads.append(x)
                x.start()
            for thread in threads:
                thread.join()
        else:
            parsing(link, wait, search, rows)
    except Exception as name:
        quit()