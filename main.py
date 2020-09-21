import numpy as np
import pandas as pd

df = pd.DataFrame({'a': range(100), 'b': range(100)})

def add_column(df):
    df['new'] = df.apply(lambda row: row['a'] + row['b'], axis = 1)
    return df

add_column(df)
#print(df)
