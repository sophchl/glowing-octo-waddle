# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:12:49 2020

@author: Sophia
"""

## helpful commands
#%reset 
#clear
#type()

## functions

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
