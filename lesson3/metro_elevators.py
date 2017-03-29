import csv
from datetime import datetime, date


metro_elevators_repair = {}
with open ('data-397-2017-02-08.csv', 'r', encoding = 'utf8') as metro_stations:
    reader = csv.DictReader(metro_stations, delimiter=';')
    for row in reader:
        if row['Ремонт эскалаторов']:
            metro_elevators_repair[row['Наименование']] = row['Ремонт эскалаторов']
        

today = datetime.now()
print('Сегодня {} идет ремонт эскалаторов на станциях:'.format(datetime.strftime(today, '%d.%m.%Y')))
for station, dates in metro_elevators_repair.items():
    repair_dates = dates.split('-', maxsplit=1)
    start_date, finish_date = dates.split('-', maxsplit=1)
    start_date = datetime.strptime(start_date, '%d.%m.%Y')
    finish_date = datetime.strptime(finish_date, '%d.%m.%Y')
    if today >= start_date and today <= finish_date:
        print(station)



