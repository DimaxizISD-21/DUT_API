import requests
from bs4 import BeautifulSoup
from utils import getKeyValueOption, clean_data, output_week



def get_faculty(url):
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            faculty = {}

            main_form = soup.find('form', attrs={'id': 'filter-form'}) 
            for element in main_form:
                faculty_el = element.find('select', attrs={'id': 'TimeTableForm_faculty'})

                # Перебираем key/value для faculty
                getKeyValueOption(faculty, faculty_el)

                # Очистка данных
                clean_data(faculty)

            return faculty


def get_course(url):
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            course = {}

            main_form = soup.find('form', attrs={'id': 'filter-form'}) 
            for element in main_form:
                course_el = element.find('select', attrs={'id': 'TimeTableForm_course'})

                # Перебираем key/value для course
                getKeyValueOption(course, course_el)

                # Очистка данных
                clean_data(course)

            return course


def get_group(url):
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            group = {}

            main_form = soup.find('form', attrs={'id': 'filter-form'}) 
            for element in main_form:
                group_el = element.find('select', attrs={'id': 'TimeTableForm_group'})

                # Перебираем key/value для group
                getKeyValueOption(group, group_el)

                # Очистка данных
                clean_data(group)

            return group


def next_parse(next_url):
    pass


def e_rozklad_parser(url):
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
           
            # Список для сохранения дней недели
            weekdays = []

            # Списки для сохранения расписания по неделям
            week_1 = []
            week_2 = []
            week_3 = []
            week_4 = []
            week_5 = []

            main_table = soup.find('table', attrs={'id': 'timeTableGroup'})

            # Делаем вывод с Пн по Пт
            x = (len(main_table.findAll('tr')) - 2)
            for row in main_table.findAll('tr')[0:x]:
                col = row.findAll('td')
                day_week = col[0].div.text
                first_week = col[1].getText().replace(' ', '')
                second_week = col[2].getText().replace(' ', '')
                third_week = col[3].getText().replace(' ', '')
                fourth_week = col[4].getText().replace(' ', '')
                fifth_week = col[5].getText().replace(' ', '')

                weekdays.append(day_week)
                week_1.append(first_week)
                week_2.append(second_week)
                week_3.append(third_week)
                week_4.append(fourth_week)
                week_5.append(fifth_week)

                # print(row.find('div', attrs={'class': 'cell mh-50'})['data-content'].text)
                # new_dict['first_week'].append(first_week)
                # new_dict['second_week'].append(second_week)
                # new_dict['third_week'].append(third_week)
                # new_dict['fourth_week'].append(fourth_week)
                # new_dict['fifth_week'].append(fifth_week)
            
           
            # Выводим в консоли например 1 неделю
            print()
            output_week(weekdays, week_1)

            # Вывод расписания в формате JSON
            e_rozklad = [{
                'first_week': week_1,
                'second_week': week_2,
                'third_week': week_3,
                'fourth_week': week_4,
                'fifth_week': week_5,
            }]
            # print(e_rozklad) 