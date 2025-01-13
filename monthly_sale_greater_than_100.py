import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import os

file_path = "Bonarco Sales-2024.xlsx"
dataa = pd.read_excel(file_path)

# Columns to check 
columns_to_check = [140210, 140211, 140212, 140301, 140302, 140303, 140304, 140305, 140306, 140307, 140308, 140309]
dataa.set_index(dataa.columns[0], inplace=True)
filtered_data = dataa[columns_to_check]

# Identify rows where at least one column has a value greater than or equal to 100
rows_to_keep = (filtered_data >= 100).any(axis=1)
# Keep the full rows from the original DataFrame
filtered_rows = dataa[rows_to_keep].copy()  # Explicitly create a copy
# Add a new column to count how many columns have values greater than or equal to 100
filtered_rows['Count >= 100'] = (filtered_data[rows_to_keep] >= 100).sum(axis=1)

# Save
filtered_rows.to_excel("filtered_rows_greater_than_100.xlsx", index=True)
print("Filtered rows saved to 'filtered_rows_greater_than_100.xlsx' with the new count column.")
