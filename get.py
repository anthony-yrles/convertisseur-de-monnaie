from forex_python.converter import CurrencyRates
import json

def get_country_data():
    c = CurrencyRates()
    rates = c.get_rates('')
    country_data = dict(rates)
    return country_data

def copy_country_data(country_data):
    return dict(country_data)

def get_country_names(country_json):
    country_data = json.loads(country_json)
    return list(country_data.keys())

def get_country_rates(country_json, currency_enter, currency_output):
    country_data = json.loads(country_json)
    if currency_enter not in country_data or currency_output not in country_data:
        return None
    rate_enter = country_data[currency_enter]
    rate_output = country_data[currency_output]
    return rate_output / rate_enter