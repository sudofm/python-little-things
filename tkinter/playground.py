def add(*args):
    result = 0
    for n in args:
        result += n
    return result

print(add(1,5,6,))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(4, add=2, multiply=3)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car( model="GT-R")
print(my_car.model)