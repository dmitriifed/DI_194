"""
GenAI-ML / Week02 / Day3 / ExerciseXP

Instructions:
- Write your solution below.
- Add tests in a __main__ block.
"""

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        return f"{self.amount} {self.currency}s"
    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return f"Currency('{self.amount}', {self.currency}"
    
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                     f"Cannot add between Currency"
                     f"<{self.currency} and {other.currency}"
            )
        return Currency(self.currency, self.amount + other.amount)
    
    def __iadd__(self, other):
         if isinstance(other, int):
            self.amount += other
            return self
         if isinstance(other, Currency):
            if self.currency != other.currency:
               raise TypeError(
                f"Cannot add between Currency "
                f"<{self.currency}> and <{other.currency}>"
            )
            self.amount += other.amount
            return self

       


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
print(str(c1))
print(int(c1))

# def main():
#     pass

# if __name__ == "__main__":
#     main()
