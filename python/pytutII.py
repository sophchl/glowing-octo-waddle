# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 08:52:15 2020

@author: Sophia
"""
# setup
import numpy as np
import pandas as pd

#%% Numpy Arrays

# Numpy arrays: alternative to lists
# advantages: fast, easy, perform calculations over entire arrays

# create first 2 lists
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# create numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# perform calculations and subset
bmi = np_weight / np_height **2
bmi > 23
bmi[bmi > 23]

# ex: convert list to array, convert weight from kg to pounds (2.2 lbs per kilogram)

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)


#%% Pandas Basics

# panda: data manipulation tool, builds on numpy package and key data structure is DataFrame, allow stora and manipulate tabular data in rows and columns

# one way to create a data frame: use a dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dict)
print(brics)

# changing the index
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

# another way to create data frame: import
cars = pd.read_csv('cars.csv')

# indexing data frames
cars = pd.read_csv('cars.csv', index_col = 0) # import without index

# print out model column as Pandas series or Pandas DataFrame, print rows
print(cars['Model'])
print(cars[['Model']])
print(cars[0:4])

# indexing rows using loc (label-based) and iloc (integer index based)
print(cars.iloc[2]) # second column
print(cars.loc[['Acura']]) # all rows that contain Acuras



