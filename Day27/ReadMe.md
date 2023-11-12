## Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs

What have I learned? 
- Graphical User Interface (GUI) with Tkinter and Function Arguments (Default Arguments,
*Args, **Kwargs)

Advanced Python Arguments - a way to specify a wider range of inputs 
1. Arguments with default values: 
def my_function(a=1,b=2,c=3):
   #Code
Calling a functon with default values
my_function()
Calling a function with different value of specified argument:
my_function(b=99)

2. Functions with Unlimited Arguments 
def add(*args):
    for n in args:
        print(n)
args - is a form of a tuple 

**kwarg - keyword argument, that allows to pass to the function keyword arguments. It is like a Dictionary 

We can initialize an object with **kwargs:
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")
But a difference between a kwargs["make"] and kwargs.get("make) is that:
When a user did not specify the key called make the dict["make"] will throw an error and dict.get("make") will return None

