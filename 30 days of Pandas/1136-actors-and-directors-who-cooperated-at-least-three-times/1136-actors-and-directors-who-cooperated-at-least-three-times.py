import pandas as pd

def actors_and_directors(df: pd.DataFrame) -> pd.DataFrame:

    df = df.groupby(['actor_id','director_id'])['timestamp'].count().reset_index()

    return df[df['timestamp']>=3][['actor_id','director_id']]
    