import numpy as np
import pandas as pd

# # fruit_data = {
# #     'apple_sales': [3, 2, 0, 2, 9, 4, 7, 2],
# #     'orange_sales': [0, 3, 2, 7, 7, 8, 3, 0 ]
# # }

# # purchases = pd.DataFrame(fruit_data, index=['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Day8'])

# # print(purchases.head())

# ### Importing Files into Pandas
# # Read a CSV, excel, json, sql, html, xml, clipboard, etc. file into a DataFrame
# # Read Employee into a DataFrame
# employee_df = pd.read_csv('data/Employee.csv')
# employee_df.head()  
# rows, columns = employee_df.shape
# print('Rows:', rows)
# print('Columns:', columns)

# # Importing a json Data 
# cars_df = pd.read_json('data/Cars.json')
# cars_df.head()

# rows, columns = cars_df.shape
# print('Rows:', rows)    
# print('Columns:', columns)

# cars_df.dtypes

# ## EDA- Exploratory Data Analysis-The first look
#   #- Data Profiling

# cars_df.describe()       
# cars_df.count()
# cars_df.info()


# #---------------------------------------------------------------------------
# student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
# student_df = pd.DataFrame(student_dict,)
# student_df.head()
# student_df.describe()

# list_index = student_df.columns
# print("Column Names:", list_index)

# Label= student_df.columns[0]
# print(Label) 

# #Getting the column names as a list for looping
# labels_as_list = student_df.columns.tolist()
# print(labels_as_list)   

# #----------------------------------------------------------------------------------------
# # EDA w\CSV
# e_df=pd.read_csv('data/Employee.csv')
# e_df.head() 
# e_df.describe()     
# e_df.count()
# e_df.info() 
# e_df.tail()

# rows, columns = e_df.shape
# print('Rows:', rows)
# print('Columns:', columns)  

# e_df=pd.read_csv('data/Employee.csv', skiprows=5, header=None, names=['ID', 'Name', 'Department', 'Salary']     )
# e_df2 = pd.read_csv('data/Employee.csv', skiprows=[0, 2, 4])
# e_df.head() 
# e_df2.head()


# # Get only specific columns from the CSV file
# e_df3 = pd.read_csv('data/Employee.csv', usecols=['Name', 'Salary'])
# e_df3.head()

# # SELECTING COLUMNS USING PENDAS

# df_cars = pd.read_json('data/Cars.json')
# df_cars.head()
# # Select only the 'Make' and 'Model' columns           
# df_cars_columns= df_cars[[0, 1, 9]]
# df_cars_columns.head()

# df_cars['car']

# df_cars[df_cars_columns[0]]

# df_cars[['car',  'mpg', 'quantity']]

# df_cars[df_cars.columns[[0, 1, 9 ]]]      

#------------------------------------------------------------------------------------------------------------------------------------
# FREQUENCY/ANALYSIS-VALUE COUNTS

# Sample DataFrame
data = {'Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Books', 'Clothing']}
cat_df = pd.DataFrame(data)
# Calculate frequency counts for the 'Category' column
cat_df.value_counts()

#CREATE DATAFRAMEE

# Create the dataframe
sales_data={"Devices":['Laptop','iPhone','LED','LCD','Smart-Phone','Washing-Machine'],
           'Brand':['Lenovo','Apple','Samsung','Samsung','Samsung','Whirpool'],
           'Sales':[1000,2000,4000,2000,1000,4000],
           'Profit':[500,1000,1000,1500,1000,1500],
           'Pices left':[5000,4000,4000,5000,5000,1000]}

sales_df=pd.DataFrame(sales_data)
frequency_counts = sales_df['Brand'].value_counts()
print(frequency_counts) 

frequent_product= sales_df[sales_df['Brand'].isin(frequency_counts[frequency_counts > 1].index)]
print(frequent_product)
print(f'This item appears more than once: {frequent_product}')

data = {'Score': [85, 92, 88, 75, None, 90, None, 85]}
score_df = pd.DataFrame(data)
score_counts = score_df['Score'].value_counts(dropna=False)
print(score_counts) 

