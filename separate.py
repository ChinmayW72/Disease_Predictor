import pandas as pd

# Assuming your data is stored in a CSV file named 'your_file.csv'
file_path = 'Original_Medical.csv'
data = pd.read_csv(file_path)

# Split the 'Blood Pressure' column
data[['Systolic_BP', 'Diastolic_BP']] = data['Blood Pressure'].str.split('/', expand=True)

# Drop the original 'Blood Pressure' column
data = data.drop(columns=['Blood Pressure'])

# Save the modified DataFrame to a new CSV file
output_file_path = 'modified_data.csv'
data.to_csv(output_file_path, index=False)

# Display a message indicating the file has been saved
print(f"The modified data has been saved to {output_file_path}")
