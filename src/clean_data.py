import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    df = df.drop_duplicates()

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df.fillna({
        'name': 'Unknown',
        'age': df['age'].median(),
        'email': 'noemail@example.com'
    }, inplace=True)

    return df

if __name__ == "__main__":
    df = pd.read_csv("raw_data.csv")
    clean_data(df).to_csv("cleaned_data.csv", index=False)
    print("Data cleaned and saved to 'cleaned_data.csv'")

