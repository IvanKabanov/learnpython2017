from datetime import datetime, timedelta

#Напечатать вчера
yesterday = datetime.now() - timedelta (days = 1)
yesterday = yesterday.strftime('%d.%m.%Y')
print('Вчера было {}'.format(yesterday))

#Напечатать сегодня
dt_now = datetime.now()
print('Сегодня {}'.format(dt_now.strftime('%d.%m.%Y')))

#Месяц назад
month_ago = datetime.now() - timedelta (days = 365/12)
month_ago = month_ago.strftime('%d.%m.%Y')
print('Месяц назад: {}'.format(month_ago))

#Превратите строку "01/01/17 12:10:03.234567" в объект datetime
datestring = '01/01/17 12:10:03.234567' 
date = datetime.strptime(datestring, '%d/%m/%y %H:%M:%S.%f')
print(date)


