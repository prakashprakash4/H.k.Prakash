import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Create Sample Customer Data
data = {
    "Customer_ID": range(1, 101),
    "Age": [random.randint(18, 60) for _ in range(100)],
    "Gender": [random.choice(["Male", "Female"]) for _ in range(100)],
    "City": [random.choice(["Hyderabad", "Bangalore", "Chennai", "Mumbai"]) for _ in range(100)],
    "Income": [random.randint(20000, 100000) for _ in range(100)],
    "Spending_Score": [random.randint(1, 100) for _ in range(100)]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display First 5 Rows
print(df.head())

# Set Style
sns.set(style="whitegrid")

# Create Dashboard
plt.figure(figsize=(15, 10))

# 1. Age Distribution
plt.subplot(2, 2, 1)
sns.histplot(df["Age"], bins=10, kde=True)
plt.title("Age Distribution")

# 2. Gender Count
plt.subplot(2, 2, 2)
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")

# 3. City Distribution
plt.subplot(2, 2, 3)
sns.countplot(x="City", data=df)
plt.title("Customers by City")
plt.xticks(rotation=45)

# 4. Income vs Spending Score
plt.subplot(2, 2, 4)
sns.scatterplot(x="Income", y="Spending_Score", hue="Gender", data=df)
plt.title("Income vs Spending Score")

plt.tight_layout()
plt.show()

# Basic Analysis
print("\nAverage Age:", df["Age"].mean())
print("Average Income:", df["Income"].mean())
print("Average Spending Score:", df["Spending_Score"].mean())
