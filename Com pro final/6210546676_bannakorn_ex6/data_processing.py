import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max temperatures of all the
    cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp. The size of the
    returned dictionary must equal the number of countries represented.
    """
    d = dict()
    for country in country_list(cities_data):
        t = []
        for r in cities_data:
            if r['country'] == country:
                t.append(float(r['temperature']))
        d[country] = sum(t) / len(t)
    return d


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and maximum city temperatures differ the most in the following format: (the country whose minimum and maximum city temperatures differ the most, min temperature, max temperature, max temperature - min temperature)
    """
    countries = []
    for country in country_list(cities_data):
        temp_dict = {}
        temp_list = []
        for r in cities_data:
            if r['country'] == country:
                temp_list.append(float(r['temperature']))
        temp_dict['min_temp'] = min(temp_list)
        temp_dict['max_temp'] = max(temp_list)
        temp_dict['diff_temp'] = float(max(temp_list)) - float(min(temp_list))
        temp_dict['country'] = country
        countries.append(temp_dict)
    most_diff = 0
    for country_dict in countries:
        if country_dict['diff_temp'] > most_diff:
            most_diff = country_dict['diff_temp']
    for country_dict in countries:
        if country_dict['diff_temp'] == most_diff:
            return country_dict['country'], country_dict['min_temp'], country_dict['max_temp'], country_dict[
                'diff_temp']


def northern_sounthern_most_cities(cities_data):
    """Returns a list of tuples with information about the northernmost and southernmost cities together with their associated countries in the following format: [(northernmost city, its country), (southernmost city, its country)]
    """
    latitude = []
    for country in country_list(cities_data):
        for r in cities_data:
            if r['country'] == country:
                latitude.append(float(r['latitude']))
    northernmost = max(latitude)
    southernmost = min(latitude)
    lst = []
    for country in cities_data:
        if float(country['latitude']) == northernmost:
            lst.append((country['city'], country['country']))
        if float(country['latitude']) == southernmost:
            lst.append((country['city'], country['country']))
    return lst


def population_countries_no_coastline_in_EU(countries_data):
    """Returns a dictionary whose keys are countries in EU but do not have coastline; the value associated with each key is the population of that country
    """
    population_dict = {}
    for country in countries_data:
        if country['EU'] == 'yes' and country['coastline'] == 'no':
            population_dict[country['country']] = float(country['population'])
    return population_dict


def cities_in_EU(cities_data, countries_data):
    """Returns a dictionary whose key:value pair is "name of city":"EU membership", e.g., "Graz":"yes" or 'Aalborg':'no'; the size of the dictionary must equal the number of cities represented in cities_data
    """
    # Hint:
    # Use nested for in loops to generate the dictionary:
    #
    # for city in cities_data:
    #    for country in countries_data:
    cities_in_EU_dict = {}
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                cities_in_EU_dict[city['city']] = country['EU']
    return cities_in_EU_dict


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the cities in EU countries, the average temperature of all the cities not in EU countries)
    """
    temp_in_EU = []
    temp_not_in_EU = []
    for city in cities_data:
        for country in countries_data:
            if city['country'] == country['country']:
                if country['EU'] == 'yes':
                    temp_in_EU.append(float(city['temperature']))
                if country['EU'] == 'no':
                    temp_not_in_EU.append(float(city['temperature']))
    return sum(temp_in_EU) / len(temp_in_EU), sum(temp_not_in_EU) / len(temp_not_in_EU)


# open Players.csv file with csv.DictReader and read its content into a list of dictionary, players_data
players_data = []
with open('Players.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        players_data.append(r)

# open Teams.csv file with csv.DictReader and read its content into a list of dictionary, teams_data
teams_data = []
with open('Teams.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams_data.append(r)


def average_passes(players_data):
    """Returns a tuple with four elements; the first, second, third, and fourth elements show the average number of passes made by defenders, midfielders, forwards, and goalkeepers, respectively
    """
    defenders = []
    midfielders = []
    forwards = []
    goalkeepers = []
    for player in players_data:
        if player['position'] == 'defender':
            defenders.append(float(player['passes']))
        if player['position'] == 'midfielder':
            midfielders.append(float(player['passes']))
        if player['position'] == 'forward':
            forwards.append(float(player['passes']))
        if player['position'] == 'goalkeeper':
            goalkeepers.append(float(player['passes']))
    return sum(defenders) / len(defenders), sum(midfielders) / len(midfielders), sum(forwards) / len(forwards), sum(
        goalkeepers) / len(goalkeepers)


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """
    team_list = []
    for team in teams_data:
        team_dict = {'team': team['team'], 'ratio': float(team['goalsFor']) / float(team['goalsAgainst'])}
        team_list.append(team_dict)
    most_ratio = 0
    for team in team_list:
        if float(team['ratio']) > most_ratio:
            most_ratio = float(team['ratio'])
    for team in team_list:
        if float(team['ratio']) == most_ratio:
            return team['team']


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20, plays
    less than 200 minutes and makes more than 100 passes; the format for each tuple is (player's surname, team played
    for, team ranking, minutes played, number of passes)
    """

    # Reminder: Convert minutes and passes to integers before comparing to values
    lst = []
    for player in players_data:
        for team in teams_data:
            if player['team'] == team['team'] and int(team['ranking']) <= 20 and int(player['minutes']) < 200 and int(
                    player['passes']) > 100:
                lst.append((player['surname'], player['team'], team['ranking'], player['minutes'], player['passes']))
    return lst


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a team and its passes per minute value generated by its players
    """
    lst = []
    for team in teams_data:
        passes = 0
        minutes = 0
        for player in players_data:
            if player['team'] == team['team']:
                passes += int(player['passes'])
                minutes += int(player['minutes'])
        lst.append((team['team'], passes / minutes))
    return lst


# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_married_women_embarked(place_embarked, age_threshold, titanic_data):
    """Returns the number of married women over age_threshold embarked at place_embarked
    >>> number_married_women_embarked('Cherbourg', 30, titanic_data)
    12
    >>> number_married_women_embarked('Queenstown', 25, titanic_data)
    2
    >>> number_married_women_embarked('Southampton', 40, titanic_data)
    26
    >>> number_married_women_embarked('Southampton', 35, titanic_data)
    35
    >>> number_married_women_embarked('Cherbourg', 25, titanic_data)
    14
    
    """
    count = 0
    for people in titanic_data:
        if not people['age'] == '':
            if float(people['age']) > age_threshold and people['embarked'] == place_embarked and people[
                'gender'] == 'F' and \
                    people['first'].startswith('Mrs.'):
                count += 1
    return count


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    >>> class_survival_rate(1, titanic_data)
    0.6296296296296297
    >>> class_survival_rate(2, titanic_data)
    0.47282608695652173
    >>> class_survival_rate(3, titanic_data)
    0.24236252545824846

    """
    survivor = 0
    num_people = 0
    for people in titanic_data:
        if int(people['class']) == passenger_class:
            if people['survived'] == 'yes':
                survivor += 1
            num_people += 1
    return survivor / num_people


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders

    >>> gender_survival_number('M', titanic_data)
    109
    >>> gender_survival_number('F', titanic_data)
    233
    """
    count = 0
    for people in titanic_data:
        if people['gender'] == passenger_gender and people['survived'] == 'yes':
            count += 1
    return count


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e., same last name, same
    age, same place of embarkment, and age is under 18; each tuple has the following format:
    (person1's "last name" + "first name", person2's "last name" + "first name")
    """
    lst = []
    i = 0
    for people1 in titanic_data[i:]:
        for people2 in titanic_data[i + 1:]:
            if people1['age'] != '' and people2['age'] != '':
                if people1['last'] == people2['last'] and people1['age'] == people2['age'] and people1['embarked'] == \
                        people2['embarked'] and float(people1['age']) < 18 and float(people2['age']) < 18:
                    lst.append((f'{people1["last"]} {people1["first"]}', f'{people2["last"]} {people2["first"]}'))
        i += 1
    return lst
