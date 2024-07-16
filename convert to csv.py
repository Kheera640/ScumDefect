import pandas as pd
import numpy as np

# Replace 'C:\ml\processed data\OP.xlsx' with the actual path to your Excel file
input_excel_path = r'C:\ml\processed data\12Sep6PM_modified.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(input_excel_path)

# Specify the column to sample
input_sample = 'AVG'

# Sample the data into a 2D array with each row having 200 columns
sampled_data = [df[input_sample][i:i+200].tolist() for i in range(0, len(df), 200)]

# Convert the 2D array to a DataFrame
sampled_df = pd.DataFrame(sampled_data)

# Save the sampled DataFrame to a new CSV file
output_csv_path = r'C:\ml\processed data\x_12Sep6PM.csv'
sampled_df.to_csv(output_csv_path, index=False)


