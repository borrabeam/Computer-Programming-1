import data_processing as dp
import matplotlib.pyplot as plt

# Scatter plot of cities showing latitudes versus temperatures
x = []
y = []
for city in dp.cities_data:
    x.append(float(city['latitude']))
    y.append(float(city['temperature']))
plt.xlabel('latitude')
plt.ylabel('temperature')
plt.scatter(x, y)
plt.show()

# Bar chart showing average temperatures of all cities in each country
bars = [] # list of countries
temperature = [] # average temperature of each country
dict = dp.average_country_temp(dp.cities_data)
for key, value in dict.items():
    bars.append(key)
    temperature.append(value)

numbars = len(bars)
width = .75
plt.bar(range(numbars), temperature, width, align='center')
plt.xlabel('country')
plt.ylabel('temperature')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(temperature)
plt.show()

# Pie chart showing number of EU countries versus non-EU countries
numEU = 0
numNotEU = 0
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU +=1
plt.pie([numEU, numNotEU], labels=['EU','not EU'], autopct='%1.1f%%')
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline


# your code here

# my_dict = sorted(country.item(),key = lambda item: float(item[0]))
country = sorted(list(dp.population_countries_no_coastline_in_EU(dp.countries_data).keys()))
population = sorted(list(dp.population_countries_no_coastline_in_EU(dp.countries_data).values()))


plt.bar(range(len(country)), population, align="center")
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(range(len(country)), country)
print(country)
print(population)
plt.show()



# Pie chart showing number of EU cities versus non-EU cities

# your code here
numEU = 0
numNotEU = 0
for city in dp.cities_data:
    for country in dp.countries_data:
        if city['country'] == country['country']:
            if country['EU'] == 'yes':
                numEU += 1
            else:
                numNotEU +=1
plt.pie([numEU, numNotEU], labels=['EU','not EU'], autopct='%1.1f%%')
plt.show()

# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)

# your code here
min_play = []
passes_made = []

goalkeeper_x = []
defender_x = []
midfielder_x =[]
forward_x = []

goalkeeper_y = []
defender_y = []
midfielder_y =[]
forward_y = []

# goalkeeper_list = []
# defender_list = []
# midfielder_list = []
# forward_list = []

for player in dp.players_data:
    # min_play.append(float(player['minutes']))
    # passes_made.append(float(player['passes']))
    if player['position'] == 'goalkeeper':
        # goalkeeper_list.append(min_play,passes_made)
        goalkeeper_x.append(float(player['minutes']))
        goalkeeper_y.append(float(player['passes']))
    elif player['position'] == 'defender':
        # defender_list.append(min_play,passes_made)
        defender_x.append(float(player['minutes']))
        defender_y.append(float(player['passes']))
    elif player['position'] == 'midfielder':
        # midfielder_list.append(min_play,passes_made)
        midfielder_x.append(float(player['minutes']))
        midfielder_y.append(float(player['passes']))
    elif player['position'] == 'forward':
        # forward_list.append(min_play,passes_made)
        forward_x.append(float(player['minutes']))
        forward_y.append(float(player['passes']))

plt.xlabel('minutes')
plt.ylabel('passes')
# plt.scatter(min_play, passes_made)
# plt.scatter(goalkeeper_list, color = "yellow")
# plt.scatter(defender_list, color = "blue")
# plt.scatter(midfielder_list, color = "green")
# plt.scatter(forward_list, color = "red")

plt.scatter(goalkeeper_x,goalkeeper_y, color = "yellow")
plt.scatter(defender_x,defender_y, color = "blue")
plt.scatter(midfielder_x,midfielder_y, color = "green")
plt.scatter(forward_x,forward_y, color = "red")
plt.show()

# Bar chart showing average number of passes made by each player postion (defender, midfielder, forward, goalkeeper)

# your code here
position = ['defender', 'midfielder', 'forward', 'goalkeeper']
average_pass = dp.average_passes(dp.players_data)
plt.bar(range(len(position)), average_pass, width=0.75, align='center')
plt.xlabel('Position')
plt.ylabel('Average passes')
plt.xticks(range(len(position)), position)
print(position)
print(average_pass)
plt.show()


# Bar chart showing the survival rate in each passenger class; the three bars should be labeled 'first', 'second', 'third'

# your code here

position = ['first', 'second', 'third']
average_pass = dp.class_survival_rate(1,dp.titanic_data),dp.class_survival_rate(2,dp.titanic_data),dp.class_survival_rate(3,dp.titanic_data)
plt.bar(range(len(position)), average_pass, width=0.75, align='center')
plt.xlabel('passenger class')
plt.ylabel('survival rate')
plt.xticks(range(len(position)), position)
print(bars)
print(average_pass)
plt.show()

# Pie chart showing the number of male survivors versus female survivors

# your code here
# male = 0
# female= 0
# for gender in dp.titanic_data:
#     if gender['survived'] == 'yes':
#         if gender['gender'] == 'M':
#             male += 1
#         else:
#             female +=1
#     else: pass
male = dp.gender_survival_number('M',dp.titanic_data)
female = dp.gender_survival_number('F',dp.titanic_data)
plt.pie([male, female], labels=['male','female'], autopct='%1.1f%%')
plt.show()