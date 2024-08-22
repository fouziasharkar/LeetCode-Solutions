import pandas as pd

def nth_highest_salary(df: pd.DataFrame, N: int) -> pd.DataFrame:
    cond = df['salary'].sort_values(ascending = False).drop_duplicates()

    if N>len(cond) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    nth_salary = cond.iloc[N-1]
    #return pd.DataFrame({f'getNthHighestSalary({N})':[nth_salary]})
    return pd.DataFrame({"getNthHighestSalary({})".format(N): [nth_salary]})
    
