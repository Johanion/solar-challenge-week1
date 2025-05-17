# summary statics and missing value report 

import pandas as pd

df = pd.read_csv("data/sierraleone-bumbuna.csv")  
df.describe()

# Missing values
missing = df.isna().sum()
missing_percent = (missing / len(df)) * 100
missing_report = missing[missing_percent > 5]
print("Columns with >5% missing:", missing_report)
