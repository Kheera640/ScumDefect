import pandas as pd

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = r'C:\ml\processed data\2Aug3am_modified.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Apply RMS to the 'DL_Tension' column and create a new column 'DL_Tension_RMS'
df['DL_Tension_RMS'] = df['DL_Tension'].apply(lambda x: x**2).rolling(window=len(df), min_periods=1).mean().apply(lambda x: x**0.5)

# Save the DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)
