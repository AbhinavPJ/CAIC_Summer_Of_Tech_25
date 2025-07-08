import pandas as pd
input_file = 'training_raw.csv'      
output_file = 'training.csv'
df = pd.read_csv(input_file, low_memory=False)

print("== Initial Dataset Info ==")
print(f"Total rows: {len(df)}")
print(f"Columns: {list(df.columns)}\n")
print("== Missing Values ==")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0], "\n")
print("== Invalid Date Formats ==")
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # coerce invalid to NaT
invalid_dates = df['date'].isnull().sum()
print(f"Invalid 'date' entries: {invalid_dates}\n")
print("== Non-numeric Likes ==")
df['likes'] = pd.to_numeric(df['likes'], errors='coerce')  # coerce to NaN
invalid_likes = df['likes'].isnull().sum()
print(f"Invalid 'likes' entries: {invalid_likes}\n")
print("== Duplicates ==")
full_duplicates = df.duplicated().sum()
print(f"Fully duplicated rows: {full_duplicates}")
id_duplicates = df['id'].duplicated().sum() if 'id' in df.columns else 0
print(f"Duplicate IDs: {id_duplicates}\n")
df.dropna(subset=['date', 'likes', 'content', 'username'], inplace=True)
df.drop_duplicates(inplace=True)
if 'id' in df.columns:
    df = df.drop_duplicates(subset='id')
df['likes'] = df['likes'].astype(int)
df['username'] = df['username'].astype(str)
df.to_csv(output_file, index=False)
print(f"\n✅ Cleaned dataset saved to: {output_file}")
print(f"✅ Final row count: {len(df)}")
