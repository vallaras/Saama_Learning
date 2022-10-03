import pandas as pd
import numpy as np
from pandas import Series

arr = Series([15, 35, 55, 75])
print(arr)

print('\nValues in this Array     : ',arr.values)
print('Index Values of this Array : ',arr.index)

arr1 = Series([25, 50, 75, 100, 125], index=[2, 4, 6, 8, 10])
print(arr1)

print('\nValues in this Array     : ', arr1.values)
print('Index Values of this Array : ', arr1.index)

arr2 = Series([2, 33, 66, 70, 15], index = ['a', 'e', 'i', 'o', 'u'])
print(arr2)
print('\nValues in this Array     : ', arr2.values)
print('Index Values of this Array : ', arr2.index)

arr4 = Series(np.arange(6))
print(arr4) # print(arr)

# Here, we are assigning the index names.
arr5 = Series(np.arange(6), index = ['a', 'b', 'c', 'd', 'e', 'f'])
print(arr5)

new_arr = Series([2, 33, 66, 70, 15], index=['a', 'e', 'i', 'o', 'u'])
print(new_arr)
print('\nValues in this Array     : ', new_arr.values)
print('Index Values of this Array : ', new_arr.index)
print(' ')

# Assigning New Index Values
new_arr.index = [1, 2, 3, 4, 5]
print(new_arr)
print('\nValues in this Array     : ', new_arr.values)
print('Index Values of this Array : ', new_arr.index)

f_dict = {'apples': 500, 'kiwi': 20, 'oranges': 100, 'cherries': 6000}
print('Dictionary Items')
print(f_dict)

arr = Series(f_dict)
print('\nArray Items')
print(arr)

f_dict = {'apples': 500, 'kiwi': 20, 'oranges': 100, 'cherries': 6000}
new_list = ['apples', 'cherries', 'kiwi', 'oranges']

arr = Series(f_dict, index=new_list)
print('Array Items')
print(arr)

f_dict = {'apples': 500, 'kiwi': 20, 'oranges': 100, 'cherries': 6000}
new_list = ['apples', 'banana', 'cherries', 'kiwi', 'oranges']

arr = Series(f_dict, index=new_list)
print('Array Items')
print(arr)

arr1 = Series([22, 44, 66, 88, 108])
print(arr1)
print(arr1[0])
print(arr1[4])

arr1 = Series([22, 33, 44, 55], index = ['a', 'b', 'c', 'd'])
print(arr1)

print('b' in arr1)
print('c' in arr1)
print('f' in arr1)

arr5 = Series([2, 4, -6, 8, -7], index = ['a', 'e', 'i', 'o', 'u'])
arr5

print(arr5+3)


#data fram programs

data = pd.DataFrame()
print(data)

table = [1, 266, 3, 455, 5]

data = pd.DataFrame(table)
print(data)

table = [[1, 'Suresh'], [2, 'Python'], [3, 'Hello']]

data = pd.DataFrame(table)
print(data)

table = [[1, 'Suresh'], [2, 'Python'], [3, 'Hello']]
data = pd.DataFrame(table, columns = ['S.No44444', 'Name'])
print(data)

d_frame = pd.DataFrame(np.random.randn(8, 4))
print(d_frame)

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Salary': [1000000, 1200000, 900000, 1100000]
         }

data = pd.DataFrame(table)
print(data)

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [25, 32, 30, 26],
         'Profession': ['Developer', 'Analyst', 'Admin', 'HR'],
         'Salary':[1000000, 1200000, 900000, 1100000]
         }

data = pd.DataFrame(table)
print(data)

names = ['John', 'Mike', 'Suresh', 'Tracy']
ages = [25, 32, 30, 26]
Professions = ['Developer', 'Analyst', 'Admin', 'HR']
Salaries = [1000000, 1200000, 900000, 1100000]

table = {'name': names,
         'Age': ages,
         'Profession': Professions,
         'Salary': Salaries
         }

data = pd.DataFrame(table)
print(data)

dates = pd.date_range('20190101', periods = 8)
print(dates)
print()

d_frame = pd.DataFrame(np.random.randn(8, 4), index = dates,
                       columns = {'apples', 'oranges', 'kiwis', 'bananas'})
print(d_frame)

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [25, 32, 30, 26],
         'Profession': ['Developer', 'Analyst', 'Admin', 'HR'],
         'Salary':[1000000, 1200000, 900000, 1100000]
         }

data1 = pd.DataFrame(table)
print(data1)

print('\n---- After Changing the Column Order-----')
data2 = pd.DataFrame(table, columns = ['name', 'Profession', 'Salary', 'Age'])
print(data2)

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [25, 32, 30, 26],
         'Salary':[1000000, 1200000, 900000, 1100000]
       }

data = pd.DataFrame(table)
print(data)
print('\n---Shape or Size of a DataFrame---')
print(data.shape)

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [25, 32, 30, 26],
         'Profession': ['Developer', 'Analyst', 'Admin', 'HR'],
         'Salary':[1000000, 1200000, 900000, 1100000]
         }

data2 = pd.DataFrame(table, columns = ['name', 'Profession', 'Salary', 'Age'])

data3 = pd.DataFrame(table, columns = ['name', 'Qualification', 'Salary', 'Age'])

print('---Data2 Values--- ')
print(data2.values)

print('\n---Data3 Values--- ')
print(data3.values)

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [25, 32, 30, 26],
         'Profession': ['Developer', 'Analyst', 'Admin', 'HR'],
         'Salary':[1000000, 1200000, 900000, 1100000]
         }

data1 = pd.DataFrame(table)
print(data1)

print('\n---describe function result---')
print(data1.describe())

table = {'name': ['John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [25, 32, 30, 26],
         'Profession': ['Developer', 'Analyst', 'Admin', 'HR'],
         'Salary':[10000, 12000, 9000, 11000]
         }

data1 = pd.DataFrame(table)
data2 = pd.DataFrame(table, columns = ['name', 'Profession', 'Salary', 'Age'])

print('-----Accessing DataFrame Columns-----')
print(data1.Age)
print(data1['name'])
print(data2.Salary)

#We can also access multiple DataFrame columns
print('-----Accessing Multiple DataFrame Columns-----')
print(data1[['Age', 'Profession']])
print(data2[['name', 'Salary']])


table = {'name': ['Kane', 'John', 'Suresh', 'Tracy', 'Steve'],
         'Age': [35, 25, 32, 30, 29],
         'Profession': ['Manager', 'Developer', 'Analyst', 'Admin', 'HR'],
         'Sale':[422.19, 22.55, 119.470, 200.190, 44.55],
         'Salary':[12000, 10000, 14000, 11000, 14000]
       }
data = pd.DataFrame(table)
print(data)

print('\n---Select all rows from 1 to N in a DataFrame---')
print(data[1:])

print('\n---Select rows from 1 to 2 in a DataFrame---')
print(data[1:3])

print('\n---Select rows from 0 to 3 in a DataFrame---')
print(data[0:4])

print('\n---Select last row in a DataFrame---')
print(data[-1:])

table = {'name': ['Kane', 'Suresh', 'Tracy'],
         'Age': [35, 25, 29],
         'Profession': ['Manager', 'Developer', 'HR'],
         'Salary': [10000, 14000, 11000],
         'basic': [4000, 6000, 4500]
        }

data = pd.DataFrame(table)
print(data)

# Add New Column to DataFrame
data['Sale'] = [422.19, 200.190, 44.55]
print('\n---After adding New Column DataFrame---')
print(data)

# Add New Column using existing
data['Income'] = data['Salary'] + data['basic']
print('\n---Total Salary in a DataFrame---')
print(data)

# Add New Calculated Column to DataFrame
data['New_Salary'] = data['Salary'] + data['Salary'] * 0.25
print('\n---After adding New Column DataFrame---')
print(data)


table = {'name': ['Kane', 'Suresh', 'Tracy'],
         'Age': [35, 25, 29],
         'Profession': ['Manager', 'Developer', 'HR'],
         'Salary': [10000, 14000, 11000],
         'basic': [4000, 6000, 4500],
         'Sale': [422.19, 200.190, 44.55]
        }

data = pd.DataFrame(table)
print(data)

# Delete existing Columns from DataFrame
del(data['basic'])
print('\n---After Deleting basic Column DataFrame---')
print(data)

x = data.pop('Age')
print('\n---After Deleting Age Column DataFrame---')
print(data)
print('\n---pop Column from DataFrame---')
print(x)

y = data.drop(columns = 'Sale')
print('\n---After Deleting Sale Column DataFrame---')
print(y)


table = {'name': ['Kane', 'Suresh', 'Tracy'],
         'Profession': ['Manager', 'Developer', 'HR'],
         'Salary': [10000, 14000, 11000],
         'Sale': [422.19, 200.190, 44.55]
        }

data = pd.DataFrame(table, index = ['a', 'b', 'c'])
print(data)

x = data.drop('b')
print('\n---After Deleting b row DataFrame---')
print(x)

y = data.drop('a')
print('\n---After Deleting a row DataFrame---')
print(y)

table = {'name': ['Kane', 'John', 'Mike', 'Suresh', 'Tracy', 'Steve'],
         'Age': [35, 25, 32, 30, 26, 29],
         'Profession': ['Manager', 'Developer', 'Analyst', 'Admin', 'HR', 'HOD'],
         'Sale':[422.19, 22.55, 12.66, 119.470, 200.190, 44.55],
         'Salary':[12000, 10000, 8000, 14000, 11000, 14000]
       }
data = pd.DataFrame(table)
print(data)

print('\n---First Five records DataFrame head()---')
print(data.head())

print('\n---First two records DataFrame head(2)---')
print(data.head(2))

print('\n---Bottom Five records DataFrame tail()---')
print(data.tail())

print('\n---last two records DataFrame tail(2)---')
print(data.tail(2))


table = {'name': ['Kane', 'Dave', 'Ram', 'John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [35, 25, 25, 35, 25, 35, 35],
         'Profession': ['Analyst', 'HR', 'Analyst', 'Admin', 'HR', 'Admin', 'HR'],
         'Sale':[422, 22, 55, 12, 119, 470, 200],
         'Salary':[12000, 9000, 10000, 8000, 14000, 20000, 11000]
       }
data = pd.DataFrame(table)

grouped_data1 = data.groupby('Profession').sum()
stacked_data1 = grouped_data1.stack()
print('\n---Stacked DataFrame groupby Profession---')
print(stacked_data1)

grouped_data2 = data.groupby(['Profession', 'Age']).sum()
stacked_data2 = grouped_data2.stack()
print('\n---Stacked DataFrame groupby Profession and Age---')
print(stacked_data2)

table = {'name': ['Kane', 'John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [35, 25, 32, 30, 26],
         'Profession': ['Manager', 'Developer', 'Analyst', 'Admin', 'HR'],
         'Sale':[422.19, 22.55, 12.66, 119.470, 200.190],
         'Salary':[12000, 10000, 8000, 14000, 11000]
       }
data = pd.DataFrame(table)
print(data)

print('\n---DataFrame Mean of Columns---')
print(data.mean())

print('\n---DataFrame Mean of Rows---')
print(data.mean(1))

print('\n---DataFrame Median of Columns---')
print(data.median())

print('\n---DataFrame Median of Rows---')
print(data.median(1))

table = {'name': ['Kane', 'John', 'Mike', 'Suresh', 'Tracy'],
         'Age': [35, 25, 32, 30, 26],
         'Profession': ['Manager', 'HR', 'Analyst', 'Manager', 'HR'],
         'Sale':[422.19, 22.55, 12.66, 119.470, 200.190],
         'Salary':[12000, 10000, 8000, 14000, 11000]
       }
data = pd.DataFrame(table)
print(data)
# load DataFrame to text file
data.to_csv('user_info.txt')
# load DataFrame to csv file with comma separator
data.to_csv('user_info.csv')
# load data from DataFrame to csv file with Tab separator
data.to_csv('user_info_new.csv', sep = '\t')

table = {'name': ['Kane', 'John', 'Mike'],
         'Age': [35, 25, 32],
         'Profession': ['Manager', 'HR', 'Analyst'],
         'Sale':[422.19, 119.470, 200.190],
         'Salary':[12000, 14000, 11000]
       }
data = pd.DataFrame(table)
print(data)
print('\n---Iterating Rows---')
for rows, columns in data.iterrows():
    print(rows, columns)
    print()
