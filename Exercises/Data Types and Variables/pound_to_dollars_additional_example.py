from forex_python.convertor import CurrencyRates

amount = int(input('Amount in GBP:'))
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = amount * current_rate
print(f'{amoun} GBP is {result:.3f} USD')