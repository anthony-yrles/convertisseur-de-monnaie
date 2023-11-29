from forex_python.converter import CurrencyCodes

def convert(amount, rate, state_output):
    total_convert = amount * rate
    symbol = CurrencyCodes()
    symbol = symbol.get_symbol(state_output)
    total = f"{total_convert:.2f} {symbol}"

    return(total)