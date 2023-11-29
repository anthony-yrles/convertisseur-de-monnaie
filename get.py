from forex_python.converter import CurrencyRates

def get_country_names():
    c = CurrencyRates()
    rates = c.get_rates('')
    country_names = list(rates.keys())

    return country_names

def get_country_rates(state_enter, state_output):
    c = CurrencyRates()
    rates = c.get_rate(state_enter, state_output)

    return rates