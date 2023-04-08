import pandas as pd

gdp_file_path = "economical_factors.xlsx"
gdp_df = pd.read_excel(gdp_file_path, sheet_name='quarterly')

# Convert 'DATE' column to datetime type
gdp_df['DATE'] = pd.to_datetime(gdp_df['DATE'])
# Rename the coloumns for uniformity and clarity
#TODO figure out why renaming doesn't work
gdp_df.rename(columns={gdp_df.columns[0]:'date', gdp_df.columns[1]:'gdp_rate'})

snp_file_path = "s&p500.xlsx"
snp_df= pd.read_excel(snp_file_path, sheet_name="SnP")

# Convert 'Date' column to datetime type
snp_df['Date'] = pd.to_datetime(snp_df['Date'])
snp_df.rename(columns={snp_df.columns[0]:'date', snp_df.columns[1]:'snp_rate'})

covid_file_path = "us_covid.csv"
covid_df = pd.read_csv(covid_file_path)

# Convert 'date' column to datetime type
covid_df['date'] = pd.to_datetime(covid_df['date'])

#drop all unneccesary collumns from covid data, keep only date and contraction rate
#TODO ask Edward, do we want the covid contraction rate as the "new cases per million"
covid_df = covid_df.iloc[:, [3,11]]
covid_df.rename(columns={covid_df.columns[0]: 'date', covid_df.columns[1]:'contraction_rate'})

print(gdp_df)
print(snp_df)
print(covid_df)
