import csv
cities_data = []
with open('cities.csv','r',encoding='ISO-8859-1') as f:
    rows = csv.reader(f)
    for r in rows:
        cities_data.append(r)
       
# print(cities_data[0:10])
# print(cities_data[8:10])

city_temp_tuple = []
for i in cities_data:
    city_temp_tuple.append((i[0],i[4]))
    # city_temp_tuple.append()
# fill in the code yourself
# print(city_temp_tuple)
