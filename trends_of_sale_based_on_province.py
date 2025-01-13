import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import os

file_pathh = "total_sale_prov.xlsx"  
dataa = pd.read_excel(file_pathh)

columns_to_sum = [140210, 140211, 140212, 140301, 140302, 140303, 140304, 140305, 140306, 140307, 140308, 140309, 'Total']
dataa.set_index(dataa.columns[0], inplace=True)

# Filter 
filtered_data = dataa[columns_to_sum]
output_folder = "prov"
os.makedirs(output_folder, exist_ok=True)

# Create a bar chart for each row in the filtered DataFrame
for index, row in filtered_data.iterrows():
    # Ensure the row contains numeric data 
    row_numeric = row.apply(pd.to_numeric, errors='coerce').dropna()

    if not row_numeric.empty:
        plt.figure(figsize=(8, 6))  
        row_numeric.plot(kind='bar', title=f"{index} Bar Chart")  
        plt.xlabel('Columns')
        plt.ylabel('Values')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save 
        chart_filename = os.path.join(output_folder, f"{index}_bar_chart.png")
        plt.savefig(chart_filename)
        plt.close()
    else:
        print(f"Row {index} does not contain valid numeric data.")
