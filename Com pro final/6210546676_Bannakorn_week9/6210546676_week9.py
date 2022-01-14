# 2
# import csv
# cities_data = []
# city_temp_tuple = []
# with open('cities.csv','r',encoding='ISO-8859-1') as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         cities_data.append(r)
#         # city_temp_tuple.append((r['city']))
#         # city_temp_tuple.append((r['latitude']))
#         city_temp_tuple.append((r['city'], r['latitude']))

# print(city_temp_tuple)


# 3
# import csv
# cities_data = []
# city_temp_tuple = []
# with open('cities.csv','r',encoding='ISO-8859-1') as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         cities_data.append(r)
#         # city_temp_tuple.append((r['city']))
#         # city_temp_tuple.append((r['latitude']))
#         city_temp_tuple.append((r['city'], r['latitude']))




# def list_countries(cities_data):
#     countries = []
#     for i in cities_data:
#         if i['country'] not in countries:
#             countries.append(i['country'])
#         else: pass
#     return countries

# countries = list_countries(cities_data)
# print(len(countries))
# print(countries)


# 4

# import csv
# cities_data = []
# city_temp_tuple = []
# with open('cities.csv','r',encoding='ISO-8859-1') as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         cities_data.append(r)
#         # city_temp_tuple.append((r['city']))
#         # city_temp_tuple.append((r['latitude']))
#         city_temp_tuple.append((r['city'], r['latitude']))




# def list_countries(cities_data):
#     countries = []
#     for i in cities_data:
#         if i['country'] not in countries:
#             countries.append(i['country'])
#         else: pass
#     return countries

# countries = list_countries(cities_data)


# def compute_ave_country_temp(countries):
#     dict1 = {}
#     avg_temp = []
#     for name in countries:
#         temp = 0
#         count = 0
#         for i in range(len(cities_data)):
#             if cities_data[i]["country"] == name:
#                 temp += float(cities_data[i]["temperature"])
#                 count += 1
#         avg_temp.append(temp/count)
#     for i in range(len(countries)):
#         dict1[countries[i]] =  avg_temp[i]
    
#     return dict1
# print(len(compute_ave_country_temp(countries)))        
# print(compute_ave_country_temp(countries))




# 5



# def read_file(file):
        

#     cities_data = []
#     city_temp_tuple = []
#     with open(file,'r') as f:
#         rows = csv.DictReader(f)
#         for r in rows:
#             cities_data.append(r)
#             # city_temp_tuple.append((r['city']))
#             # city_temp_tuple.append((r['latitude']))
#             city_temp_tuple.append((r['city'], r['latitude']))
#     return cities_data


# def extract_to_list(cities_data,v):
#     extract_list = [float(cities_data[i][v]) for i in range(len(cities_data))]
#     return extract_list



# def list_countries(cities_data):
#     countries = []
#     for i in cities_data:
#         if i['country'] not in countries:
#             countries.append(i['country'])
#         else: pass
#     return countries




# def compute_ave_country_temp(countries):
#     dict1 = {}
#     avg_temp = []
#     for name in countries:
#         temp = 0
#         count = 0
#         for i in range(len(cities_data)):
#             if cities_data[i]["country"] == name:
#                 temp += float(cities_data[i]["temperature"])
#                 count += 1
#         avg_temp.append(temp/count)
#     for i in range(len(countries)):
#         dict1[countries[i]] =  avg_temp[i]
    
#     return dict1

# import csv
# import matplotlib.pyplot as plt

# cities_data = read_file('cities.csv')
# lat = extract_to_list(cities_data,'latitude')
# long = extract_to_list(cities_data,'longitude')
# temps = extract_to_list(cities_data,'temperature')
# high = extract_to_list(cities_data,'highest')
# # Plot scatter plot using x = latitude,
# # y = temperature,
# # color=longitude
# plt.scatter(lat,temps,c=range(len(long)))
# # Add x-axis label
# plt.xlabel('Latitude')
# # Add y-axis label
# plt.ylabel('Temperatures')
# # Add label for color bar
# plt.colorbar().ax.set_title('Longtitude')
# # Save plot as image file
# plt.savefig('lat_temps_long.png')
# # Show plot
# plt.show()
# plt.scatter(long,temps,c=range(len(lat)))
# plt.xlabel('Longitude')
# plt.ylabel('Temperatures')
# plt.colorbar().ax.set_title('Latitude')
# # Set colormap to the selected one
# # See more colormap selection in the reference at the end of
# plt.set_cmap('RdBu')
# plt.savefig('long_temps_lat.png')
# plt.show()

# 6




def read_file(file):

    cities_data = []
    city_temp_tuple = []
    with open(file,'r',encoding='ISO-8859-1') as f:
        rows = csv.DictReader(f)
        for r in rows:
            cities_data.append(r)
            # city_temp_tuple.append((r['city']))
            # city_temp_tuple.append((r['latitude']))
            city_temp_tuple.append((r['city'], r['latitude']))
    return cities_data



def count_region_freq(cities_data):
    northern = 0
    western = 0
    southern = 0
    central_eastern = 0

    region = []
    freq_list = []
    
    for i in cities_data:
        if i['region'] not in region:
            region.append(i['region'])
        else: pass


    for i in range(len(cities_data)):
        if cities_data[i]['region'] == 'Northern':
            northern += 1
        elif cities_data[i]['region'] == 'Western':
            western += 1
        elif cities_data[i]['region'] == 'Southern':
            southern += 1
        elif cities_data[i]['region'] == 'Central and Eastern':
            central_eastern += 1
        else: pass

    freq_list.append(northern)
    freq_list.append(western)
    freq_list.append(southern)
    freq_list.append(central_eastern)
    
    return  region, freq_list



import csv
import matplotlib.pyplot as plt
cities_data = read_file('cities.csv')
region_list, region_freq_list = count_region_freq(cities_data)
# Set up bar colors in bar graph
# See more color names in the reference at the end of Exercise 6
my_colors = ['red','blue','green','orange']
# Plot bar graph using x = unique region list
# y = region frequency
# Bar graph color is set to my_colors list
plt.bar(region_list, region_freq_list, color=my_colors)
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.savefig('region_freq.png')
plt.show()

