import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['salary'].sort_values(ascending = False).drop_duplicates()

    if len(df)<2:
        return pd.DataFrame({"SecondHighestSalary".format():[None]})
    
    second_salary = df.iloc[1]
    return pd.DataFrame({"SecondHighestSalary".format():[second_salary]})
    