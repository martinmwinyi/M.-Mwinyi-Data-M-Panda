# CREATING A PANDAS DATABASE
import numpy as np
import pandas as pd
# Create a dictionary of data
d={'x':['1', '2', '3'], 'y':[2, 4, 8], 'z':100}
df=pd.DataFrame(d)
df2=pd.DataFrame(d, index=[100, 200, 300], columns=['y', 'z', 'x'])
df2

#students Dictionary
student_dict = {
    'Name': ['Joe', 'Nat', 'Harry'],
    'Age': [20, 21, 19],
    'Marks': [85.10, 77.80, 91.54]
}
student_df = pd.DataFrame(student_dict)
student_df.head()

student_df.dtypes

#M Make a colunns from the df into the index
student_df=student_df.set_index('Name')
print(student_df.head())

#Create Indexes using customer RangeIndex
data = {
    'Product': ['Laptop', 'Tablet', 'Phone'],
    'Price': [1200, 300, 800],
    'Quantity': [50, 150, 100]
}
df3 = pd.DataFrame(data)
df3.head()

# create a list of patientID, name, and date of birth and assign it to a variable
patientID = [101,23,48,49]
name =       ['alice','bob','charlie','Eric']
# create a list of dates
date_of_birth = ['2023-01-01', '2023-01-02', '3/10/2020 143045', '13th of October, 2023']
employee_df = pd.DataFrame(zip(patientID, name, date_of_birth), columns=['PatientID', 'Name','DateOfBirth'])
employee_df.head()

# in this example, we create a list of stocks and their prices and then create a DataFrame.
stocks = ["IBM", "APPLE", "TWTTR", "GE", "MSFT"]
prices = [115.00, 119.14, 19.77, 25.99, 26]
# create a DataFrame using the stocks and prices lists  
stock_df = pd.DataFrame(zip(stocks, prices), columns=['Stock', 'Price'])    
stock_df.head()

arr=np.array([[1, 2, 100], [2, 4, 100], [3, 8, 100]])
numpy_df=pd.DataFrame(arr, columns=['x', 'y', 'z'])
numpy_df.head()


