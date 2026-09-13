import os
import pandas as pd

print("--- Step 1: Downloading dataset ---")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(f"Original dataset shape: {df.shape}")

print("--- Step 2: Cleaning and Preprocessing ---")
# Fill missing 'Age' values with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# Drop irrelevant text columns and columns with too many missing values
df = df.drop(columns=['Cabin', 'PassengerId', 'Name', 'Ticket'])

# Fill missing 'Embarked' values with the mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Remove duplicate records
df = df.drop_duplicates()

# Encode categorical variables into numeric format
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

print(f"Cleaned dataset shape: {df.shape}")

print("--- Step 3: Saving cleaned dataset to Desktop ---")
# Automatically find the user's Desktop path across different operating systems
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "cleaned_titanic.csv")

# Save the dataframe to CSV
df.to_csv(output_file, index=False)

print(f"Success! Cleaned dataset saved to: {output_file}")