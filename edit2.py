import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = r'C:\ml\original data\OP.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Convert the "Time" column to datetime format with fractional seconds
df['Time'] = pd.to_datetime(df['Time'], format='%d.%m.%Y %H:%M:%S.%f')

# Calculate the time difference in seconds from the start of the column
df['TimeInSeconds'] = (df['Time'] - df['Time'].iloc[0]).dt.total_seconds()

# Save the DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)
