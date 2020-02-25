# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:12:49 2020

@author: Sophia
"""

## helpful commands
#%reset 
#clear
#type()

#%%
## functions

## Exercise
# Modify this function to return a list of strings as defined above
def list_benefits():
    return"More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" %(benefit)
# using print here introduces a none-line after every sentence in the last execution

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

#%%
## classes and objects

# Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.variable
myobjectx.function()

myobjecty = MyClass()
myobjecty.variable = "yackity"

## Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, 
# and car2 to be a blue van named Jump worth $10,000.00.
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000


car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000

# test code
print(car1.description())
print(car2.description())

#%%
## dictionaries
# similar to an array, but works with keys and values instead of indexes

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
# phonebook.items(), phonebook.keys(), phonebook.values()
# delete: del phonebook["John"] or phonebook.pop("John")
    
## Exercise: Add Jack(938273443) and remove Jill
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

del phonebook["Jill"]
phonebook["Jake"] = 938273443

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")


#%%
## Modules and Packages
# module: piece of software that has a specific functionality, in python: files with .py extension
# from fibo import .. (all: *), import fibo
# packages: Packages are namespaces which contain multiple packages and modules themselves. 
# They are simply directories, but with a twist.
# Each package in Python is a directory which MUST contain a special file called __init__.py

import foo.bar
from foo import bar

# print an alphabetically sorted list of all functions in the re module, which contain the word find.
import re
[i for i in dir(re) if "find" in i]

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
