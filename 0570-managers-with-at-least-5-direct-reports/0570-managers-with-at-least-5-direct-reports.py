import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee.groupby('managerId').size().reset_index(name='occurances')

    filtered_df = df[df['occurances']>=5]

    return employee.merge(filtered_df,left_on='id',right_on='managerId',how='inner').drop(columns=['id','department','managerId_x','managerId_y','occurances'])
    
    