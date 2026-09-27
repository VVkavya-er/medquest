import pandas as pd
import os


input_file = "data/patient_admissions.csv"


output_file = "data/patient_admissions_cleaned.csv"

df = pd.read_csv(input_file)

print("Original rows:", len(df))
print("Original columns:", len(df.columns))


df = df.dropna(how="all")


df = df.drop_duplicates()


df.columns = df.columns.str.strip()


text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].astype("string").str.strip()


df = df.replace(r"^\s*$", pd.NA, regex=True)


print("\nMissing values:")
print(df.isnull().sum())


df.to_csv(output_file, index=False)

print("\n--------------------------------")
print("DATA CLEANING COMPLETED")
print("--------------------------------")
print("Cleaned rows:", len(df))
print("Columns:", len(df.columns))
print("Saved file:", output_file)