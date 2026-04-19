#Use DataFrames to organize and filter information.
#Create a DataFrame representing "Employee Records": ['Name', 'Department', 'Salary'].
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Department': ['HR', 'IT', 'Finance', 'IT'],
'Salary': [50000, 60000, 55000, 65000]} 
df = pd.DataFrame(data)
print(df)
#Sort the records by Name in alphabetical order.
sorted_df = df.sort_values(by='Name')
print(sorted_df)
#Filter the data to show only employees who work in the "AI Research" department.
ai_research_df = df[df['Department'] == 'AI Research']
print(ai_research_df)
#3.Calculate the mean (average) salary of all employees in the DataFrame.
mean_salary = df['Salary'].mean()
print(f"Mean Salary: {mean_salary}")

