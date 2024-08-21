import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # Rename columns
    department.rename(columns={'id': 'departmentId', 'name': 'Department'}, inplace=True)
    employee.rename(columns={'name': 'Employee', 'salary': 'Salary'}, inplace=True)

    # Merge the employee and department DataFrames based on 'departmentId'
    df = employee.merge(department, on='departmentId')

    # Find the highest salary per department
    max_salary= df.groupby('Department')['Salary'].transform('max')

    # Filter rows where the salary is equal to the highest salary in their department
    highest_salary_employees = df[df['Salary'] == max_salary]

    # Select relevant columns
    result = highest_salary_employees[['Department', 'Employee', 'Salary']]

    return result