import numpy as np
import pandas as pd

# ==========================================
# 1. CREATING & LOADING THE DATASET
# ==========================================
data = {
    'Emp_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Role': [' Backend Developer ','data scientist','Frontend Dev',
             'Data Scientist','backend developer','DevOps',
             'Data Scientist','Backend Developer','DevOps',
             'Frontend Dev',
    ],
    'Country': ['Germany','Germany','USA','USA','UK','UK',
                'Germany','USA','Germany','UK',],
    'Experience': ['Senior','Junior','Senior','Mid',
                    'Junior','Senior','Senior','Mid',
                    'Junior','Senior',],
    'Salary_USD': [95000,55000,130000,115000,48000,
                    105000,110000,120000,52000,88000,],
    'Is_Remote': ['Yes','No','Yes','Yes','No',
                    'Yes','No','No','Yes','Yes',],
}

df = pd.DataFrame(data)

# ==========================================
# 2. DATA CLEANING & STANDARDIZATION
# ==========================================
# Question 1: Strip leading/trailing whitespaces and title case words in Role column
df['Role'] = df['Role'].str.strip().str.title()

# ==========================================
# 3. INDEXING AND FILTERING TEST
# ==========================================
# Senior and Remote employees
senior_remote = df.loc[
    (df['Is_Remote'] == 'Yes') & (df['Experience'] == 'Senior')
]

# Country-based indexing example
df_indexed = df.set_index('Country')
usa_data = df_indexed.loc['USA']

# ==========================================
# 4. GROUPING AND ANALYSIS QUESTIONS
# ==========================================

# Question 2: Group by country to calculate mean and median salaries
country_salary_summary = df.groupby('Country')['Salary_USD'].agg(
    ['mean', 'median']
)

# Question 3: Dual grouping by Role and Experience, sorted by mean salary in descending order
role_exp_salary = (
    df.groupby(['Role', 'Experience'])['Salary_USD']
    .mean()
    .sort_values(ascending=False)
)

# Question 4: Remote employee count and percentage by country
remote_counts = df.groupby('Country')['Is_Remote'].value_counts()
remote_rates = df.groupby('Country')['Is_Remote'].value_counts(
    normalize=True
)

remote_analysis = pd.DataFrame(
    {'Count': remote_counts, 'Ratio (%)': (remote_rates * 100).round(2)}
)

# Question 5: Detailed statistics table by role using .agg()
role_stats = df.groupby('Role')['Salary_USD'].agg(
    Employee_Count='count',
    Max_Salary='max',
    Min_Salary='min',
    Std_Dev='std',
)

# ==========================================
# 5. PRINTING RESULTS
# ==========================================
print("=== CLEANED DATASET ===")
print(df)
print("\n" + "=" * 50 + "\n")

print("=== 2. COUNTRY-BASED SALARY SUMMARIES (MEAN & MEDIAN) ===")
print(country_salary_summary)
print("\n" + "=" * 50 + "\n")

print("=== 3. AVERAGE SALARIES BY ROLE & EXPERIENCE LEVEL ===")
print(role_exp_salary)
print("\n" + "=" * 50 + "\n")

print("=== 4. REMOTE WORKERS COUNT AND PERCENTAGE BY COUNTRY ===")
print(remote_analysis)
print("\n" + "=" * 50 + "\n")

print("=== 5. DETAILED STATISTICAL SUMMARY BY ROLE (.agg) ===")
print(role_stats)