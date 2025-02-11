# -*- coding: utf-8 -*-
"""Project_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16oiH80LnCcZbQOCrz1JzOhkd4319NyPj
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
df = pd.read_csv("/content/Consumption of meat per capita.csv")
print(df)

# Display first few rows
print(df.head())

# Group data by year to calculate total meat consumption per year
df_global_trend = df.groupby("Year").sum().reset_index()

# Set plot style
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plot different meat types over time
for column in df_global_trend.columns[2:]:  # Exclude 'Year'
    plt.plot(df_global_trend["Year"], df_global_trend[column], label=column)

plt.xlabel("Year")
plt.ylabel("Meat Consumption (kg per capita)")
plt.title("Global Meat Consumption Trends Over Time")
plt.legend()
plt.show()

# Select a specific country (e.g.,Bangladesh) and analyze its trend
country = "Bangladesh"
df_country = df[df["Entity"] == country]

# Plot meat consumption trends for this country
plt.figure(figsize=(12, 6))
for column in df_country.columns[2:]:  # Exclude 'Country' and 'Year'
    plt.plot(df_country["Year"], df_country[column], label=column)

plt.xlabel("Year")
plt.ylabel("Meat Consumption (kg per capita)")
plt.title(f"Meat Consumption Trends in {country}")
plt.legend()
plt.show()

print(df.columns)

meat_columns = ['Entity', 'Year', 'Poultry', 'Beef', 'Sheep and goat', 'Pork',
       'Other meats', 'Fish and seafood']

# Sum of meat types
df["Total Meat"] = df[meat_columns].sum(axis=1, numeric_only=True)

# Group by country
df_country_sum = df.groupby("Entity")["Total Meat"].sum().reset_index()

# Sort by highest consumption
df_country_sum = df_country_sum.sort_values(by="Total Meat", ascending=False)
df_country_sum

top_countries = df_country_sum.nlargest(10, "Total Meat")
plt.figure(figsize=(20, 5))
plt.title(f"Top Ten Countries in Meat Consumptions")
sns.barplot(x="Entity", y="Total Meat", data=top_countries, palette="coolwarm")

import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

plt.figure(figsize=(12, 6))
sns.barplot(data=df[['Poultry', 'Beef', 'Sheep and goat', 'Pork',
       'Other meats', 'Fish and seafood']])
plt.title("Distribution of Individual Meat Consumption per Capita")
plt.xlabel("Meat Type")
plt.ylabel("Consumption (kg per capita)")
plt.xticks(rotation=45)
plt.show()

df.isnull().sum()

df['Beef'].fillna(df['Beef'].mean(), inplace = True)
df['Pork'].fillna(df['Pork'].mean(),inplace = True)
df['Other meats'].fillna(df['Other meats'].mean(),inplace = True)

df.isnull().sum()

# Splitting data into training and testing sets
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression # Importing Logistic Regression

le = LabelEncoder()
df["Entity"] = le.fit_transform(df["Entity"])
X_train, X_test, y_train, y_test = train_test_split(df.drop("Entity", axis = "columns"), df["Entity"], test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a classification model
model = LogisticRegression(max_iter=10000) # LogisticRegression
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted') # Adjust 'average' as needed
recall = recall_score(y_test, y_pred, average='weighted') # Adjust 'average' as needed
cm = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"Confusion Matrix:\n{cm}")

