# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 21:16:10 2022

@author: liese
"""
#https://data.cdc.gov/NCHS/Weekly-Provisional-Counts-of-Deaths-by-State-and-S/muzy-jte6

import pandas as pd
import matplotlib as plt

df = pd.read_csv(r'C:\Users\liese\Downloads\Career\Datasets\Weekly_Provisional_Counts_of_Deaths_by_State_and_Select_Causes__2020-2022.csv')
print(df.columns)

#print(df['citizenship'].value_counts())

# Get rid of null values (simplified)
df = df.dropna(axis='columns', thresh=5184)
df = df.dropna(axis='rows')

