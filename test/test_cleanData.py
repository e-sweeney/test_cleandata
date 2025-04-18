import pandas as pd
from src.clean_data import clean_data  # Replace with the actual module name


def clean_data(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    df = df.drop_duplicates()

    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df.fillna({
        'name': 'Unknown',
        'age': df['age'].median(),
        'email': 'noemail@example.com'
    }, inplace=True)

    return df
