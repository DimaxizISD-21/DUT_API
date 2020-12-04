# Ф-ция перебора option для элементов
def getKeyValueOption(dictionary, element):
    option = element.find_all('option')
    for val in option:
        dictionary[val.text] = val['value']


# Ф-ция, которая выводит значение по ключу
def get_DataValue(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            return v


# Ф-ция получения значения ключа, в зависимости
# от количества нумерованных значений словаря
def getSelectedIters(val_input, dictionary):
    main_key = ''
    for i , key in enumerate(dictionary):
        if i+1 == val_input:
            main_key = key
    return get_DataValue(dictionary, main_key)


# Ф-ция для очистки данных
def clean_data(dictionary):
    del dictionary['\xa0']


# Ф-ция для вывода значений ключей в нумерованном виде  
def dict_iter_list(dictionary, iters_list):
    for i, key in enumerate(dictionary):
        print(f'{i+1} : {key}')
        iters_list.append(i+1)


# Ф-ция для вывода расписания на неделю
def output_week(days, week):
    for day, week in zip(days, week):
        output_week = f'{day} -----------{week} '.replace(' ', '\n')
        print(output_week)