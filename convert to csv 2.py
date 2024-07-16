import pandas as pd
import numpy as np

# Replace 'C:\ml\processed data\OP.xlsx' with the actual path to your Excel file
input_excel_path = r'C:\ml\processed data\clustering_result.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(input_excel_path)

# Specify the column to sample for x_sample
input_sample_x = 'AVG'

# Sample the data into a 2D array with each row having 200 columns for x_sample
sampled_data_x = [df[input_sample_x][i:i+200].tolist() for i in range(0, len(df), 200)]

# Convert the 2D array to a DataFrame for x_sample
sampled_df_x = pd.DataFrame(sampled_data_x)

# Save the sampled DataFrame to a new CSV file for x_sample
output_csv_path_x = r'C:\ml\processed data\x_sample.csv'
sampled_df_x.to_csv(output_csv_path_x, index=False)

# Specify the column to sample for y_sample
input_sample_y = 'Label'

# Sample data in chunks of 200 rows from the specified column for y_sample
sampled_data_y = [df[input_sample_y][i:i+200].tolist() for i in range(0, len(df), 200)]

# Create an array where each element represents 60% of the corresponding 200 elements for y_sample
output_array_y = np.array([1 if np.sum(chunk) / 200 >= 0.6 else 0 for chunk in sampled_data_y])

# Reshape the 1D array to a 2D array with one column for y_sample
output_2d_array_y = output_array_y.reshape(-1, 1)

# Convert the 2D array to a DataFrame for y_sample
output_df_y = pd.DataFrame(output_2d_array_y, columns=['Output'])

# Save the DataFrame to a CSV file for y_sample
csv_output_path_y = r'C:\ml\processed data\y_sample.csv'
output_df_y.to_csv(csv_output_path_y, index=False)
