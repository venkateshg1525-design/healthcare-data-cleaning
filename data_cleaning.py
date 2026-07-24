import pandas as pd

# Load dataset
df = pd.read_csv("healthcare_dataset.csv")

# Display first 5 rows
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

# Dataset Information
print("\n========== DATASET INFO ==========")
print(df.info())

# Missing Values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Duplicate Rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Remove Duplicate Rows
df = df.drop_duplicates()

# Save Cleaned Dataset
df.to_csv("cleaned_healthcare_dataset.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")