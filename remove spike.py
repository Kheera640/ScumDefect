import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = r'C:\ml\processed data\OP.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Specify the threshold and replacement value
threshold = 46
replacement_value = 40

# Create a new column 'newAVG' using the IF statement
df['newAVG'] = df['AVG'].apply(lambda x: replacement_value if x >= threshold else x)

# Save the DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)
