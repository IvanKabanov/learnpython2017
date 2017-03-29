from geopy.distance import great_circle
import csv

bus_stops_dict = {}

with open ('bus_stops.csv', 'r', encoding = 'utf8') as bus_stops:
    reader = csv.DictReader(bus_stops, delimiter=';')
    for row in reader:
        coordinates_list = []
        geodata = row['geoData'].replace('\n', '')
        geodata = geodata.split()
        coordinates_list.append(float(geodata[-1].strip(']')))
        coordinates_list.append(float(geodata[-2].strip(',')))
        bus_stops_dict[row["Name"]] = coordinates_list

metro_stations_dict = {}     

with open ('data-397-2017-02-08.csv', 'r', encoding = 'utf8') as metro_exits:
    reader = csv.DictReader(metro_exits, delimiter=';')
    for row in reader:
        metro_latitute = float(row['Широта в WGS-84'])
        metro_longtitute = float(row['Долгота в WGS-84'])
        metro_stations_dict[row['Наименование']] = (metro_latitute, metro_longtitute)


bus_next_to_metro = {}

for bus_stop_coordinates in bus_stops_dict.values():
    bus_stop_coordinates = tuple(bus_stop_coordinates)
    for metro_station_name, metro_station_coordinates in metro_stations_dict.items():
        distance_between = great_circle(metro_station_coordinates, bus_stop_coordinates).m
        if distance_between <= 500:
            if metro_station_name in bus_next_to_metro:
                bus_next_to_metro[metro_station_name] += 1
            else:
                bus_next_to_metro[metro_station_name] = 1



value_numbers = []
for key, value in bus_next_to_metro.items():
    value_numbers.append(value)
    
max_stops = max(value_numbers)

for metro_stations_name, bus_stops_num in bus_next_to_metro.items():
    if bus_stops_num == max_stops:
        print('Больше всего остановок рядом с метро {}. Там {} остановок'.format(metro_stations_name, bus_stops_num))        
    
    

