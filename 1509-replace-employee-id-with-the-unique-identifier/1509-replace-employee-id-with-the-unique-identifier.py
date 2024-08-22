import pandas as pd

def replace_employee_id(df: pd.DataFrame, df1: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(df,df1,left_on='id',right_on='id',how='left')[['unique_id','name']]