import pandas as pd
from sklearn.model_selection import train_test_split

# Load your CSV dataset
dataset_filename = 'diseases1.csv'
df = pd.read_csv(dataset_filename)

# Split the dataset into training and evaluation datasets (e.g., 80/20 split)
train_df, eval_df = train_test_split(df, test_size=0.3, random_state=42)



# Define the file path for the evaluation dataset
eval_filename = 'diseases1E.csv'

# Save the evaluation dataset to a CSV file
eval_df.to_csv(eval_filename, index=False)

print(f"Evaluation dataset saved to '{eval_filename}'")
