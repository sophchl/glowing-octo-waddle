# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:12:49 2020

@author: Sophia
"""

## helpful commands
#%reset 
#clear
#type()
#os.getcwd()
#type()


#%% old stuff

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)

# your code goes here
for x in numbers:
    if(x==237):
        break
    if(x % 2 != 0):
        continue
    print(x)
    
# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)

def function_with_args(Name, Function, Wish):
    print("Hello %s, %s, I wish you %s!" %(Name, Function, Wish))
    
def list_benefits():
    return ("More organized code", "More readable code", 
            "Easier code reuse", "Allowing programmers to share and connect code together")

def build_sentence(benefit):
    return("%s is a benefit of functions!" %(benefit))
    
# first task: print numbers 1,2,3,4 from a range form (1,10), 3 versions
for i in range(1,10):
    if(i%5==0):
        break
    print(i)
    
for i in range(1,10):
    if(i==5):
        break
    print(i)

i=1
while i<5:
    print(i)
    i=i+1

# second task: from the array "numbers", print all even numbers until 237 (including 237)
for number in numbers:
    if(number==237):
        break
    if(number%2 == 1):
        continue
    else:
        print(number)

# build a code that prints out all benefits in a loop
listofbenefits = list_benefits()
listofbenefits = list_benefits()
for i in range(0,len(listofbenefits)):
    print(build_sentence(listofbenefits[i]))

#%% Lists

mylist =  []
myist.append(1)

for x in mylist:
    print(x)
    


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
    
# writing a module (doesnt work)
mygame/
mygame/game.py
mygame/draw.py

# import module objects to the current workspace (some or all)
# from .. import ..
# from .. import *

# import with custom import name
# import .. as ..

# packages: Packages are namespaces which contain multiple packages and modules themselves. 
# They are simply directories, but with a twist.
# Each package in Python is a directory which MUST contain a special file called __init__.py

# import 
import foo.bar
from foo import bar

# ex: print an alphabetically sorted list of all functions in the re module, which contain the word find.
import re

find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))


