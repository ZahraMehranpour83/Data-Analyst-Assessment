import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# Drop duplicated rows
df.drop_duplicates()

# Fill missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0])
    else:
        df[col].fillna(df[col].mean())

# Convert numeric columns
for col in df.columns:
    if df[col].dtype == "int64":
        df[col] = df[col].astype(np.int8)

# Statistics
stats = pd.DataFrame({
    "mean": df.mean(),
    "median": df.median(),
    "std": np.std(df),
    "min": df.min(),
    "max": df.max()
})

print(stats)

# Correlation
corr = df.corr()

# Plot Histograms
for col in df.columns:
    plt.figure(figsize=(6,4))
    plt.hist(df[col])
    plt.title(col)

# Violin Plot
plt.figure(figsize=(8,6))
plt.violinplot(df.select_dtypes(include=np.number))
plt.show()

# Remove outliers
for col in df.select_dtypes(include=np.number):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    df = df[(df[col] > q1 - 1.5 * iqr) &
            (df[col] < q3 + 1.5 * iqr)]

print(df.info())