import pandas as pd
import numpy as np

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = 'your_file.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Convert DataFrame to a 2D array with 1024 columns
array_2d = df.to_numpy().reshape(-1, 1024)

# Print or use the resulting 2D array as needed
print(array_2d)
