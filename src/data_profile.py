import pandas as pd

data_path = 'data/raw/games.csv'

df = pd.read_csv(data_path)

print("Number of rows and columns:")
print(df.shape)

print("\nNames of columns and data types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicated values:")
print(df.duplicated().sum())

print("\nValues of victory status:")
print(df["victory_status"].value_counts(dropna=False))

print("\nFirst five rows:")
print(df.head())