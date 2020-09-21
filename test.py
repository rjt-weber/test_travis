import pytest
from main import add_column
import pandas as pd

def test_add_column():
    df = add_column(pd.DataFrame({'a': 1, 'b': 1}))
    print(df)
    assert df.new == 2
