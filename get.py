from forex_python.converter import CurrencyRates

def get_country_data():
    c = CurrencyRates()
    rates = c.get_rates('')
    country_data = dict(rates)
    return country_data

def copy_country_data(country_data):
    return dict(country_data)

def get_country_names(country_data):
    return list(country_data.keys())

def get_country_rates(country_data, state_enter, state_output):
    return country_data[state_output] / country_data[state_enter]