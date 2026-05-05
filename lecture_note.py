import numpy as np
import pandas as pd

# # # fruit_data = {
# # #     'apple_sales': [3, 2, 0, 2, 9, 4, 7, 2],
# # #     'orange_sales': [0, 3, 2, 7, 7, 8, 3, 0 ]
# # # }

# # # purchases = pd.DataFrame(fruit_data, index=['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Day8'])

# # # print(purchases.head())

# # ### Importing Files into Pandas
# # # Read a CSV, excel, json, sql, html, xml, clipboard, etc. file into a DataFrame
# # # Read Employee into a DataFrame
# # employee_df = pd.read_csv('data/Employee.csv')
# # employee_df.head()  
# # rows, columns = employee_df.shape
# # print('Rows:', rows)
# # print('Columns:', columns)

# # # Importing a json Data 
# cars_df = pd.read_json('data/Cars.json')
# cars_df.head()

# rows, columns = cars_df.shape
# print('Rows:', rows)    
# print('Columns:', columns)

# # cars_df.dtypes

# # ## EDA- Exploratory Data Analysis-The first look
# #   #- Data Profiling

# # cars_df.describe()       
# # cars_df.count()
# # cars_df.info()


# # #---------------------------------------------------------------------------
# # student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
# # student_df = pd.DataFrame(student_dict,)
# # student_df.head()
# # student_df.describe()

# # list_index = student_df.columns
# # print("Column Names:", list_index)

# # Label= student_df.columns[0]
# # print(Label) 

# # #Getting the column names as a list for looping
# # labels_as_list = student_df.columns.tolist()
# # print(labels_as_list)   

# # #----------------------------------------------------------------------------------------
# # # EDA w\CSV
# # e_df=pd.read_csv('data/Employee.csv')
# # e_df.head() 
# # e_df.describe()     
# # e_df.count()
# # e_df.info() 
# # e_df.tail()

# # rows, columns = e_df.shape
# # print('Rows:', rows)
# # print('Columns:', columns)  

# # e_df=pd.read_csv('data/Employee.csv', skiprows=5, header=None, names=['ID', 'Name', 'Department', 'Salary']     )
# # e_df2 = pd.read_csv('data/Employee.csv', skiprows=[0, 2, 4])
# # e_df.head() 
# # e_df2.head()


# # # Get only specific columns from the CSV file
# # e_df3 = pd.read_csv('data/Employee.csv', usecols=['Name', 'Salary'])
# # e_df3.head()

# # # SELECTING COLUMNS USING PENDAS

# # df_cars = pd.read_json('data/Cars.json')
# # df_cars.head()
# # # Select only the 'Make' and 'Model' columns           
# # df_cars_columns= df_cars[[0, 1, 9]]
# # df_cars_columns.head()

# # df_cars['car']

# # df_cars[df_cars_columns[0]]

# # df_cars[['car',  'mpg', 'quantity']]

# # df_cars[df_cars.columns[[0, 1, 9 ]]]      

# #------------------------------------------------------------------------------------------------------------------------------------
# # FREQUENCY/ANALYSIS-VALUE COUNTS

# # Sample DataFrame
# data = {'Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Books', 'Clothing']}
# cat_df = pd.DataFrame(data)
# # Calculate frequency counts for the 'Category' column
# cat_df.value_counts()

# #CREATE DATAFRAMEE

# # Create the dataframe
# sales_data={"Devices":['Laptop','iPhone','LED','LCD','Smart-Phone','Washing-Machine'],
#            'Brand':['Lenovo','Apple','Samsung','Samsung','Samsung','Whirpool'],
#            'Sales':[1000,2000,4000,2000,1000,4000],
#            'Profit':[500,1000,1000,1500,1000,1500],
#            'Pices left':[5000,4000,4000,5000,5000,1000]}

# sales_df=pd.DataFrame(sales_data)
# frequency_counts = sales_df['Brand'].value_counts()
# print(frequency_counts) 

# frequent_product= sales_df[sales_df['Brand'].isin(frequency_counts[frequency_counts > 1].index)]
# print(frequent_product)
# print(f'This item appears more than once: {frequent_product}')

# data = {'Score': [85, 92, 88, 75, None, 90, None, 85]}
# score_df = pd.DataFrame(data)
# score_counts = score_df['Score'].value_counts(dropna=False)
# print(score_counts) 

# ## CONVERTING PANDAS COLUMNS TO LIST
# import numpy as np
# import pandas as pd

# df=pd.read_json('data/Cars.json')
# df.head()

# # Convert a column to a list
# car_list = df['Car'].tolist()
# print(car_list)

# # made a list of all values in a 'car' column
# col_list= df['Car'].values.tolist()
# print(col_list)

# #Same things but with dot syntax 
# df.Car.values.tolist()

# # Rename a Colomn in Pandas
# tech = {
#     'Courses': ["Python", ' DataAnalytics', 'MERN Stack', 'Data Engineering'],
#     'Fee': [100, 2000, 250, 300],
#     'Duration':['40days', '50days', '3 months', '1 year']
# }
# tech_df = pd.DataFrame(tech)
# tech_df = tech_df.rename(columns={'Courses': 'Course'})
# tech_df.head()

# # SORTING USING PANDAS
# data = {'Name': ['Jane', 'Princi', 'James', 'Fadi'],
#         'Height': [5.1, 6.2, 5.1, 5.2],
#         'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
#        'Score 1' : [56,86,77,45],
#        'Score 2' : [50,96,60,30]}

# grade_df = pd.DataFrame(data)
# grade_df.head()

# grade_df=grade_df.assign(address=['NY', 'LA', 'Chicago', 'Houston'])
# grade_df.head()
# print(grade_df.sort_values(by='Score 1'))    
# print(grade_df.sort_values(by='Score 1', ascending=False))

# cars= pd.read_json('data/Cars.json')
# cars.head(15)

# print(cars.sort_values(by='quantity', ascending=True))
# print(cars.sort_values(by=['quantity', 'Car'], ascending=[False, True]))

# ## Slicing a database using loc and iloc

# # Initializing the nested list with Data set
# employee_list = [['James', 36, 75, 5428000],
#                ['Villers', 38, 74, 3428000],
#                ['VKole', 31, 70, 8428000],
#                ['Smith', 34, 80, 4428000],
#                ['Gayle', 40, 100, 4528000],
#                ['Rooter', 33, 72, 7028000],
#                ['Peterson', 42, 85, 2528000],
#                ['John', 41, 85, 1528000],

# ]

# e_df = pd.DataFrame(employee_list, columns=['Name', 'Age', 'weight', 'Salary'])
# e_df.head()
# e_df.loc[:1]  

# # Get the first 3 rows of the DataFrame and all rows
# e_df.loc[: , :2]

# # Basketball players data

# basketball = {'team': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
#                    'points': [18, 22, 19, 14, 14, 11, 20, 28],
#                    'assists': [5, 7, 7, 9, 12, 9, 9, 4],
#                    'rebounds': [11, 8, 10, 6, 6, 5, 9, 12],
#                    'steals': [4, 3, 3, 2, 5, 4, 3, 8],
#                    'blocks': [1, 0, 0, 3, 2, 2, 1, 5]}

# basketball_df = pd.DataFrame(basketball)
# basketball_df.head()
# # Rows 3 to 6 and columns from 'points' to 'rebounds' and show the team name as well
# basketball_df.loc[3:6, 'team':'rebounds']
# print(basketball_df.loc[3:6, ['team', 'points', 'rebounds']])
#---------------------------------------------------------------------------------------------------------------------------------------------

# Having missing values in the DataFrame

## Pandas Data Time Series.
# date_range = pd.date_range(start='07-01-2022', end='05-05-2026', periods=7)
# print(date_range)   

# date_range2 = pd.date_range(start='01-01-2020', end='05-05-2026', freq='QE')
# print(date_range2)

# date_range3 = pd.date_range(start='01-01-2020', end='05-05-2026', periods=6, tz='Asia /Tokyo')
# print(date_range3)


# start_date ='01-01-2023'
# num_days = 30
# date_range4 = pd.date_range(start=start_date, periods=num_days, freq='D')
# print(date_range4)
# np.random.seed(42)
# stock_prices = np.random.normal(loc=100, scale=5, size=(30,))
# stock_df = pd.DataFrame({'Date': date_range4, 'Stock Price': stock_prices}) 

# stock_df=pd.DataFrame({'Date': date_range4, 'Stock Price': stock_prices})
# print(stock_df) 

#----------------------------------------------------------------------------------------------------------------------------------------------------

start_date = '01/01/2023'
num_days=30

date_range = pd.date_range(start=start_date, periods=num_days, freq='D')

np.random.seed(42) # seed means we are all using the SAME random algorithm
# mean - 100
# std - 5
# 30 numbers
stock_prices = np.random.normal(loc=100, scale=5, size=num_days).round(2)

stock_df = pd.DataFrame({'Date': date_range, 'StockPrice':stock_prices})

stock_df.head()

input_list = ['2023-01-01', '2023-01-02', '3/10/2020 143045', '13th of October, 2023']
print(input_list)
output_dates = pd.to_datetime(input_list, format='mixed')   
print(output_dates)

df = pd.DataFrame({
    'patientID':[101,23,48,49],
    'name': ['alice','bob','charlie','Eric'],
    'date_of_birth': ['2023-01-01', '2023-01-02', '3/10/2020 143045', '13th of October, 2023']
})
df.info()
df['date_of_birth'] =df['date_of_birth'].astype('datetime64[ns]')       
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='mixed')
print(df)



url='https://raw.githubusercontent.com/bprasad26/lwd/master/data/tesla_stock_prices.csv'
tesla_df = pd.read_csv(url)
tesla_df.head() 





