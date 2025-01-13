import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import os

file_path = "Bonarco Sales-2024.xlsx"
dataa = pd.read_excel(file_path)

# Columns to check for non-NaN values
columns_to_check = [140210, 140211, 140212, 140301, 140302, 140303, 140304, 140305, 140306, 140307, 140308, 140309]
dataa.set_index(dataa.columns[0], inplace=True)

# Filter the DataFrame to include only these columns for non-NaN counting
filtered_data = dataa[columns_to_check]
# Count the non-NaN values
non_nan_count = filtered_data.notna().sum(axis=1)
# Add the count as a new column 
dataa['Non-NaN Count'] = non_nan_count
# Filter rows based on the Non-NaN Count
month_data = {
    f"{i}_month": dataa[dataa['Non-NaN Count'] == i]
    for i in range(1, 13)  # From 1 to 12
}

# Save 
output_file = "n_month.xlsx"
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for sheet_name, df in month_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Data saved to {output_file} with separate sheets for each month.")
