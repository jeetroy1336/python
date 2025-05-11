import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV
df = pd.read_csv("csvfile.csv")

# Step 2: Display basic DataFrame info
print(df.info())

# Step 3: Print number of missing values in each column
print(df.isnull().sum())

# Step 4: Fill missing values
# Fill AGE with mean AGE, SCORE with mean SCORE
df['AGE'].fillna(df['AGE'].mean(), inplace=True)
df['SCORE'].fillna(df['SCORE'].mean(), inplace=True)

# Step 5: Scatter plot
plt.scatter(df['AGE'], df['SCORE'], color='red')
plt.xlabel('AGE')
plt.ylabel('SCORE')
plt.title('AGE vs SCORE COMPARISION')
plt.grid(True)
plt.show()

