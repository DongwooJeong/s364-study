import pandas as pd
import numpy as np
print("-------e1--------")
s1 = pd.Series([0.1, 0.3, 0.5, 0.7], ['a','b','c','d'])
print(s1, s1.values, s1.index)
print("-------e2--------")
d = {'Chris': '555-1111', 
     'Katie': '555-2222', 
     'Jack': '555-3333'}
s3 = pd.Series(d)
print(s3)
print(s1[1])
print("-------e3--------")
print(s3[0:2])
print(s3[['Jack', 'Katie']])
print("-------e4--------")
data = {'state': ['Ohio', 'Texas', 'Ohio'],
        'year': [2000, 2000, 2001],
        'pop': [1.5, 2.4, 1.7]}
row = [1,2,3]
frame = pd.DataFrame(data, index = row)
print(frame)
print("-------e4--------")
data2 = np.random.normal(0,1,(3,3))
col = ['A','B','C']
frame2 = pd.DataFrame(data2, index = row, columns = col)
print(frame2)
print("-------e5--------")
exdata = np.random.randint(low = -5,high = 5,size = (3,3))
exrow = ["#1","#2","#3"]
excol = ["Cost", "Return", "Rate"]
exframe = pd.DataFrame(exdata, index = exrow, columns = excol)
print(exframe)
