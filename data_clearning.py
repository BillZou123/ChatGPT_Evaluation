import pandas as pd

# Read the Excel file
file_path = 'data_Java.xlsx'
df = pd.read_excel(file_path)

# Clean the data
df_clean = df[df['Answers by ChatGPT'].notnull() & (df['Answers by ChatGPT'].str.strip() != '')]

df_clean_correct = df_clean[df_clean['error_message']=="None"]

# Calculate the statistics
total_correct = df_clean_correct.shape[0]
total_records = df_clean.shape[0]
correct_percentage = (total_correct / total_records) * 100

# Print the results
print("For Java language:")
print(f"Total records: {total_records}")
print(f"Total correct: {total_correct}")
print(f"Percentage of correct answers: {correct_percentage:.2f}%")

total_easy = df_clean[df_clean['Difficulty'] == 'Easy'].shape[0]
total_medium = df_clean[df_clean['Difficulty'] == 'Medium'].shape[0]
total_hard = df_clean[df_clean['Difficulty'] == 'Hard'].shape[0]

correct_easy = df_clean_correct[df_clean_correct['Difficulty'] == 'Easy'].shape[0]
correct_medium = df_clean_correct[df_clean_correct['Difficulty'] == 'Medium'].shape[0]
correct_hard = df_clean_correct[df_clean_correct['Difficulty'] == 'Hard'].shape[0]

# Calculate the percentage of correct answers for each difficulty level
percentage_easy = (correct_easy / total_easy) * 100
percentage_medium = (correct_medium / total_medium) * 100
percentage_hard = (correct_hard / total_hard) * 100

# Print the results
print(f"Percentage of correct answers for Easy problems: {percentage_easy:.2f}%")
print(f"Percentage of correct answers for Medium problems: {percentage_medium:.2f}%")
print(f"Percentage of correct answers for Hard problems: {percentage_hard:.2f}%")
