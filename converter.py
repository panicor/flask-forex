
class Converter():
    
    def __init__(self, to_curr, from_curr, amount):
        from forex_python.converter import CurrencyRates
        self.rates = CurrencyRates()

        self.to_curr = to_curr
        self.from_curr = from_curr
        self.amount = amount

    def converted(self):
      
        new_amt = self.rates.convert(self.to_curr, self.from_curr, self.amount)

        return new_amt
