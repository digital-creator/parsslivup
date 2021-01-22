def write_file(search,data):
    with open(f'lists_{search}.csv', 'a', encoding='utf-8') as file:
        for keys in data.keys():
            file.write(keys + ',' + data[keys] + '\n')
