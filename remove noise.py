import pandas as pd
import pywt

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_file_path = r'C:\ml\processed data\OP.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Specify the column to denoise
column_to_denoise = 'DL_Tension'

# Set the denoising threshold
threshold = 0.005 # Adjust as needed

# Apply wavelet denoising to the specified column
df['Denoised_Data'] = pywt.threshold(df[column_to_denoise], value=threshold, mode='soft')

# Save the DataFrame with denoised data to a new Excel file
output_excel_path = r'C:\ml\processed data\denoised_data.xlsx'
df.to_excel(output_excel_path, index=False)
