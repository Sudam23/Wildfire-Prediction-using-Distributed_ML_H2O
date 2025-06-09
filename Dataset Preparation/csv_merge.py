import pandas as pd
import glob
import os

# Set the folder where your CSVs are located
folder_path = '/home/sysadm/Videos/our_proj_data '  # change this!
# Use glob to find all CSV files in the folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Read and concatenate all CSVs
df_list = [pd.read_csv(file) for file in csv_files]
merged_df = pd.concat(df_list, ignore_index=True)

# Save the merged DataFrame to a new CSV
merged_df.to_csv('merged_output.csv', index=False)

print("All CSV files have been merged into 'merged_output.csv'")



##......................................Alternative Code.........................................##

import pandas as pd
import os

# Path to the folder containing your CSV files
folder_path = '/home/sysadm/Videos/H2O_cluster/ our_proj_data '

# Get list of all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# List to hold all DataFrames
df_list = []
total_original_rows = 0  # To count all rows before merge

# Read and append each CSV to the list
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    total_original_rows += len(df)
    df_list.append(df)

# Concatenate all DataFrames
merged_df = pd.concat(df_list, ignore_index=True)

# Save to a new CSV file
merged_df.to_csv('merged.csv', index=False)

# Count rows in merged file
merged_rows = len(merged_df)

# Final report
print("✅ All CSV files merged successfully into 'merged.csv'")
print(f"📦 Total rows from original CSV files: {total_original_rows}")
print(f"📄 Total rows in merged file: {merged_rows}")

if total_original_rows == merged_rows:
    print("🎉 No data lost during the merge.")
else:
    print("⚠️ Data mismatch! Rows lost or duplicated during merge.")
