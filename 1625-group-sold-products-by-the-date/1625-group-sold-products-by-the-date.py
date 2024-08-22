import pandas as pd

def categorize_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby('sell_date').agg(
        num_sold=('product', 'nunique'),
        products = ('product',lambda x:",".join(sorted(x.unique())))  

    ).reset_index()
    return df

    