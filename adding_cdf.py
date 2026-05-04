import numpy as np
import pandas as pd 

data = {'Name': ['Jane', 'Princi', 'James', 'Fadi'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
        'Score 1' : [56,86,77,45],
        'Score 2' : [50,96,60,30]}
df = pd.DataFrame(data)
print('Data frame before New Columsn')
df.head()

adress = ['NY', 'LA', 'Chicago', 'Houston']
df['Address'] = adress

print('Data frame after adding Address column')
df.head()

## OLd Columns
print('before columns')
df.head()

df['Total Score'] = df['Score 1'] + df['Score 2']
print('after adding Total Score column:')
df.head()

df['Average Score'] = df['Total Score'] / 2
df.head()

## Importing Specified Columns AND Rearrange the columns

data = {'Name': ['Jane', 'Princi', 'James', 'Fadi'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
        'Score 1' : [56,86,77,45],
        'Score 2' : [50,96,60,30]}

df2= pd.DataFrame(data, columns=['Score 1','Score 2','Name', 'Qualification']) 
print(df2)
#-------------------------------------------------------------------------

values = [['Rohan', 455], ['Elvish', 250], ['John', 495],
          ['Sai', 400], ['Eric', 350], ['Adam', 450]]
df3 = pd.DataFrame(values, columns=['Name', 'Univ_Marks'])

df3.head()

# Will compute the percentage of the umiversity marks 
df3['Percentage'] = (df3['Univ_Marks'] / 500) * 100

df3.head()

## Using the insert function to add a column in a specific location

df3.insert(1, 'Age', [1000, 2000, 50, 60, 12, 13])
df3.head()

df3=df3.assign (location=['MiddleEarth', 'Forgotten Lands', 'NYC', 'NJ', 'CA', 'MA'])
df3.head()






