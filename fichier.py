import json

def save_to_json(country_data, filename):
    with open(filename, 'w') as file:
        json.dump(country_data, file)

def read_to_json(filename):
    with open(filename, 'r') as file:
        preferences=json.load(file)
        return(preferences)