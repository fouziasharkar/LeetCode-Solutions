import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['event_day'] = pd.to_datetime(employees['event_day'])
    #employees.set_index('event_day',inplace=True)
    employees['month'] = employees['event_day'].dt.month
    employees.sort_values(by='month',inplace=True)
    employees['total_time'] = employees['out_time']-employees['in_time']
    df = employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index().rename(columns={'event_day':'day'})

    return df
    