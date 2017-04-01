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

max_stops_tuple = ()
max_stops = 1
for street, stops_count in streets_dict.items():
    if stops_count > max_stops:
        max_stops_tuple = (street, stops_count)
        max_stops = stops_count

print('Больше всего остановок на улице {}. Там {} остановок'.format(max_stops_tuple[0], max_stops_tuple[1]))
