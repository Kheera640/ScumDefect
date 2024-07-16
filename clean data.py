import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = r'C:\ml\processed data\12Sep6PM_modified.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Create a new column 'AVG' with the average of neighboring cells
window_size = 5
df['AVG'] = df['DL_Tension'].rolling(window=2*window_size+1, center=True).mean()

# Write the DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)
