from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    df = df.copy()  # Work on a copy to avoid side effects

    # 1. Encode categorical columns
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # 2. Scale numeric columns
    scaler = StandardScaler()
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df, label_encoders, scaler
