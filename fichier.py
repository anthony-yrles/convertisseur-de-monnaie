import json

def save_to_json(country_data, filename):
    country_json = []
    with open(filename, 'w') as file:
        json.dump(country_data, file)
    with open(filename, 'r') as file:
        country_json = file.read()
        return(country_json)

def read_to_json(filename):
    with open(filename, 'r') as file:
        preferences=json.load(file)
        return(preferences)