import csv

answers = {
        'привет': 'И тебе привет!',
        'как дела?': 'Отлично!',
        'до свидания': 'Пока',
        'что делаешь?': 'Отвечаю на глупые вопросы'
        }

with open('export.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    for key,value in answers.items():
        writer.writerow([key, value])
        
        