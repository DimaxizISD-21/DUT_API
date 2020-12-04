from parsers import get_faculty, get_course, get_group, e_rozklad_parser
from utils import getSelectedIters, dict_iter_list
from datetime import datetime, timedelta



# Настройка диапазона отображения даты для main_url
time_start = datetime.strftime(datetime.now(), "%d.%m.%Y")
time_end = datetime.strftime(datetime.now() + timedelta(days=7*5-1), "%d.%m.%Y")


def DutApi():
    base_url = 'http://e-rozklad.dut.edu.ua/timeTable/group?TimeTableForm%5Bfaculty%5D=1&TimeTableForm%5Bcourse%5D=5&TimeTableForm%5Bgroup%5D=1221&TimeTableForm%5Bdate1%5D=27.11.2020&TimeTableForm%5Bdate2%5D=16.04.2021&TimeTableForm%5Br11%5D=5&timeTable=0'
    faculty = get_faculty(base_url)
    course = get_course(base_url)


    data = {
        'faculty': faculty,
        'course': course,
    }

    # Списки количеств значений(value) для ключей data
    iters_1 = []
    iters_2 = []
    iters_3 = []


    print("\nСписок факультетов: ")
    dict_iter_list(data['faculty'], iters_1)


    print("\nСписок курсов: ")
    dict_iter_list(data['course'], iters_2)

    try:

        n_1 = int(input('\nВыберите факультет >>> '))
        if n_1 in iters_1:
            url_val_1 = getSelectedIters(n_1, data['faculty'])
        

        n_2 = int(input('\nВыберите курс >>> '))
        if n_2 in iters_2:
            url_val_2 = getSelectedIters(n_2, data['course'])
        
        
        # Формирование паттерна ссылки в зависимости 
        # от введенных пользователем значений 
        url_pattern =  f'http://e-rozklad.dut.edu.ua/timeTable/group?TimeTableForm%5Bfaculty%5D={url_val_1}&TimeTableForm%5Bcourse%5D={url_val_2}'


        # Запрос данных по группам
        group = get_group(url_pattern)
        data['group'] = group


        print("\nСписок групп: ")
        dict_iter_list(data['group'], iters_3)


        n_3 = int(input('\nВыберите группу >>> '))
        if n_3 in iters_3:
            url_val_3 = getSelectedIters(n_3, data['group'])


        url_main =  f'http://e-rozklad.dut.edu.ua/timeTable/group?TimeTableForm%5Bfaculty%5D={url_val_1}&TimeTableForm%5Bcourse%5D={url_val_2}&TimeTableForm%5Bgroup%5D={url_val_3}&TimeTableForm%5Bdate1%5D={time_start}&TimeTableForm%5Bdate2%5D={time_end}'

        rozklad = e_rozklad_parser(url_main)
        print()

    except ValueError:
        print("Вы ввели не число!")

    except UnboundLocalError:
        print("Вы ввели число не указанное в списке!")

DutApi()
   