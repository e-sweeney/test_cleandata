import pandas as pd

def clean_data(df):
    # 1. Normalize column names (lowercase and replace spaces with underscores)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # 2. Remove duplicate rows
    df = df.drop_duplicates()

    # 3. Strip whitespace from string columns
    str_cols = df.select_dtypes(include='object').columns
    df[str_cols] = df[str_cols].apply(lambda x: x.str.strip())

    # 4. Handle missing values
    df = df.fillna({
        'name': 'Unknown',
        'age': df['age'].median(),
        'email': 'noemail@example.com'
    })

    # 5. Convert data types
    df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Coerce invalid numbers

    return df

# Sample usage
if __name__ == "__main__":
    # Load data from CSV
    df = pd.read_csv("raw_data.csv")

    # Clean the data
    cleaned_df = clean_data(df)

    # Save cleaned data
    cleaned_df.to_csv("cleaned_data.csv", index=False)

    print("Data cleaned and saved to 'cleaned_data.csv'")
