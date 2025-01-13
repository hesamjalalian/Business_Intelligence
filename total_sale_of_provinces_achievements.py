import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

file_path = "Bonarco Sales-2024.xlsx"  
data = pd.read_excel(file_path)

names_list = data['ABDProvinceNameFA'].unique()
print(names_list)
first_name = names_list[0]
print(first_name)
filtered_dataframe = data[data['ABDProvinceNameFA'] == first_name]
print(filtered_dataframe)
total_sum = filtered_dataframe['Total'].sum()
print("The sum of the 'Total' column is:", total_sum)
most_sale = pd.DataFrame({'ABDProvinceNameFA': [first_name], 'Total_Sum': [total_sum]})
print(most_sale)

most_sale = pd.DataFrame(columns=['ABDProvinceNameFA', 'Total_Sum'])

# Loop through all names 
for name in names_list:
    # Filter the data for the current name
    filtered_dataframe = data[data['ABDProvinceNameFA'] == name]
    # Calculate the total sum 
    total_sum = filtered_dataframe['Total'].sum()
    # Add the result 
    most_sale = pd.concat([most_sale, pd.DataFrame({'ABDProvinceNameFA': [name], 'Total_Sum': [total_sum]})],
                          ignore_index=True)

print(most_sale)

plt.figure(figsize=(10, 6))
plt.bar(most_sale['ABDProvinceNameFA'], most_sale['Total_Sum'], color='skyblue')
plt.title('Total Sales by Province', fontsize=16)
plt.xlabel('Province Name', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()

most_sale = pd.read_excel('most_sale.xlsx')

plt.figure(figsize=(10, 6))
bars = plt.bar(most_sale['ABDProvinceNameFA'], most_sale['Total_Sum'], color='skyblue')

# Add 'Achievement' values 
for bar, achievement in zip(bars, most_sale['Achievement']):
    plt.text(
        bar.get_x() + bar.get_width() / 2,  
        bar.get_height() + 1,              
        str(achievement),                 
        ha='center', va='bottom', fontsize=10  
    )

plt.title('Total Sales by Province & Achievements', fontsize=16)
plt.xlabel('Province Name', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.tight_layout()
plt.show()
