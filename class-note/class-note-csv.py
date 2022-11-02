import pandas as pd
bdf = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
print(bdf.head())
print("------desc-------")
print(bdf.describe())
print("------col-------")
print(bdf[['rank', 'salary']])
print("------------------------male-----------------------")
print(bdf[ bdf['sex'] == 'Male' ])
print("-----------------------salary----------------------")
print(bdf[ bdf['salary'] > 100000 ])


nba = pd.read_csv("https://raw.githubusercontent.com/erikgregorywebb/datasets/master/nba-salaries.csv")
nbacsv = pd.read_csv("nba-salaries.csv")