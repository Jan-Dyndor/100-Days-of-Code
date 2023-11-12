
def add(*args):
    number_sum = 0
    for number in args:
        number_sum += number
    return number_sum


# print(add(2, 3, 4, 5, 6, 7, 8))
# print(add(1, 2, 3))
#

def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["muptiply"]
    print(n)


calculate(2, add=3, muptiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")
# !TODO The benefit of get() method in dictionary is that, when there is no key for example model it returns None, instead
# of throwing Error like dict["model"] would do


my_Car = Car(make="Nissan")
print(my_Car.model)
