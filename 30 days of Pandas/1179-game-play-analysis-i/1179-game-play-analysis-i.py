import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    
    # Ensure 'event_date' is in datetime format
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    
    # Rename the column
    activity.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    # Sort by 'first_login' to ensure the earliest dates come first
    activity = activity.sort_values(by='first_login')
    
    # Drop duplicate player_id, keep the first occurrence (earliest 'first_login')
    activity = activity.drop_duplicates(subset='player_id', keep='first')
    
    # Return the desired columns
    return activity[['player_id', 'first_login']]