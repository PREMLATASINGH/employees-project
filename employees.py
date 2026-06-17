import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('employees_1000.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)
print(df.groupby('department')['salary'].mean())
print(df.groupby('department')['salary'].sum())
