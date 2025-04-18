import pandas as pd
from src.clean_data import clean_data  # Replace with the actual module name


def test_clean_data():
    data = {
        'Name': [' Alice ', 'Bob', 'Alice ', None],
        'Age': ['25', None, '25', '30'],
        'Email': ['alice@example.com', 'bob@example.com', 'alice@example.com', None]
    }

    df = pd.DataFrame(data)
    cleaned = clean_data(df)

    # Check column names are normalized
    assert list(cleaned.columns) == ['name', 'age', 'email']

    # Duplicates removed: 4 rows in, 1 duplicate, expect 3 rows
    assert len(cleaned) == 3

    # Whitespace removed
    assert ' Alice ' not in cleaned['name'].values

    # Missing values filled
    assert 'Unknown' in cleaned['name'].values
    assert 'noemail@example.com' in cleaned['email'].values
    assert cleaned['age'].isnull().sum() == 0

    # Age column is numeric
    assert pd.api.types.is_numeric_dtype(cleaned['age'])