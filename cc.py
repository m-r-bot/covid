import pandas as pd

quarterly_file_path = "economical_factors.xlsx"
quarterly_df = pd.read_excel(quarterly_file_path, sheet_name='quarterly')
monthly_df = pd.read_excel(quarterly_file_path, sheet_name='monthly')

# Convert 'DATE' column to datetime type
quarterly_df['DATE'] = pd.to_datetime(quarterly_df['DATE'])
monthly_df['DATE'] = pd.to_datetime(monthly_df['DATE'])

# Set 'DATE' column as index
quarterly_df.set_index('DATE', inplace=True)
monthly_df.set_index('DATE', inplace=True)

# Resample using valid datetime index
quarterly_dates = quarterly_df.resample('BQS').asfreq('MS')

# Merge quarterly_df and monthly_df based on datetime index
merged_df = pd.merge(quarterly_dates, monthly_df, left_index=True, right_index=True, how='inner')

print(merged_df.head)

copy_merged_df = merged_df.copy

copy_merged_df = 