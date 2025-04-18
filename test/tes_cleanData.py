import pandas as pd
from src.clean_data import clean_data  # Replace with the actual module name

def test_clean_data():
    # Sample raw data
    raw_data = {
        'Name': [' Alice ', 'Bob', 'Alice ', None],
        'Age': ['25', None, '25', '30'],
        'Email': ['alice@example.com', 'bob@example.com', 'alice@example.com', None]
    }
    df = pd.DataFrame(raw_data)

    # Clean it
    cleaned = clean_data(df)

    # 1. Check column names
    assert list(cleaned.columns) == ['name', 'age', 'email']

    # 2. Should have 3 rows (one duplicate removed)
    assert len(cleaned) == 3

    # 3. Whitespace should be removed from strings
    assert cleaned.iloc[0]['name'] == 'Alice'

    # 4. Missing values filled
    assert cleaned['name'].isnull().sum() == 0
    assert cleaned['email'].isnull().sum() == 0

    # 5. Age should be numeric
    assert pd.api.types.is_numeric_dtype(cleaned['age'])

    # 6. Check specific fill value
    assert 'Unknown' in cleaned['name'].values
    assert 'noemail@example.com' in cleaned['email'].values
