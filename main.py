import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# 1️⃣ Load CSV
csv_file = "data/dataset.csv"  # Your Titanic CSV
df = pd.read_csv(csv_file)

print("Original Data (first 5 rows):")
print(df.head())

# 2️⃣ Data Cleaning
# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())         # Fill missing ages with mean
df['Embarked'] = df['Embarked'].fillna('Unknown')      # Fill missing embark info
df['Cabin'] = df['Cabin'].fillna('Unknown')            # Fill missing cabin info

# Remove duplicates (just in case)
df.drop_duplicates(inplace=True)

print("\nCleaned Data (first 5 rows):")
print(df.head())

# 3️⃣ Connect to SQLite Database
conn = sqlite3.connect("data/titanic.db")  # Database will be created here
cursor = conn.cursor()

# 4️⃣ Create Table Dynamically
columns = ', '.join([f"{col.replace(' ', '_')} TEXT" for col in df.columns])
cursor.execute(f"CREATE TABLE IF NOT EXISTS titanic ({columns})")

# 5️⃣ Insert Data into Database
df.to_sql('titanic', conn, if_exists='replace', index=False)

# 6️⃣ Generate Summary Insights
print("\nSummary Insights:")

# Total passengers
total = pd.read_sql("SELECT COUNT(*) as total_passengers FROM titanic", conn)
print(total)

# Average age
avg_age = pd.read_sql("SELECT AVG(CAST(Age AS REAL)) as avg_age FROM titanic", conn)
print(avg_age)

# Count by survival
survival_count = pd.read_sql("SELECT Survived, COUNT(*) as count FROM titanic GROUP BY Survived", conn)
print(survival_count)

# --- Plot Survival Rate ---
plt.figure(figsize=(6,4))
plt.bar(survival_count['Survived'].astype(str), survival_count['count'], color=['red','green'])
plt.title("Titanic Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.xticks([0,1], ['No','Yes'])
plt.show()

# Survival by Passenger Class
pclass_survival = pd.read_sql(
    "SELECT Pclass, Survived, COUNT(*) as count FROM titanic GROUP BY Pclass, Survived",
    conn
)
print("\nSurvival by Passenger Class:")
print(pclass_survival)

# Create a grouped bar chart
import matplotlib.pyplot as plt  # if not already imported

classes = pclass_survival['Pclass'].unique()
survived_counts = [pclass_survival[(pclass_survival['Pclass']==c) & (pclass_survival['Survived']==1)]['count'].values[0] if not pclass_survival[(pclass_survival['Pclass']==c) & (pclass_survival['Survived']==1)]['count'].empty else 0 for c in classes]
not_survived_counts = [pclass_survival[(pclass_survival['Pclass']==c) & (pclass_survival['Survived']==0)]['count'].values[0] if not pclass_survival[(pclass_survival['Pclass']==c) & (pclass_survival['Survived']==0)]['count'].empty else 0 for c in classes]

import numpy as np
x = np.arange(len(classes))
width = 0.35

plt.figure(figsize=(8,5))
plt.bar(x - width/2, not_survived_counts, width, label='Did Not Survive', color='red')
plt.bar(x + width/2, survived_counts, width, label='Survived', color='green')
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.title('Survival by Passenger Class')
plt.xticks(x, classes)
plt.legend()
plt.show()

# Count by class
class_count = pd.read_sql("SELECT Pclass, COUNT(*) as count FROM titanic GROUP BY Pclass", conn)
print(class_count)

# Close database connection
conn.close()