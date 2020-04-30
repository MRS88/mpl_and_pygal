import csv

from datetime import datetime


def get_date_list():

    f_name = 'kazan_weather_2019_04.csv'
    with open(f_name, encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # записываем все даты из столбца 0
        unsorted_dates = []
        for date in reader:
            unsorted_dates.append(date[0])

        dates = []
        for date in unsorted_dates:
            dates.append(date[:10])
            sorted_dates = list(set(dates))
            sorted_dates.sort()

        return sorted_dates


print(get_date_list())
