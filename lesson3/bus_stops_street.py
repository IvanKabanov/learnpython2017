import csv


streets_dict = {}
with open ('bus_stops.csv', 'r', encoding = 'utf8') as bus_stops:
    reader = csv.DictReader(bus_stops, delimiter=';')
    for row in reader:
        street = row['Street']
        if street in streets_dict:
            streets_dict[street] += 1
        else: 
            streets_dict[street] = 1    

value_numbers = []
for key, value in streets_dict.items():
    value_numbers.append(value)
    
max_stops = max(value_numbers)

for street, stops_count in streets_dict.items():
    if stops_count == max_stops:
        print('Больше всего остановок на улице {}. Там {} остановок'.format(street, stops_count))
