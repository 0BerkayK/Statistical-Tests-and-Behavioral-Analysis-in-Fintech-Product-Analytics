import pandas as pd

# Veri yükleme
transactions = pd.read_csv("../data/cleaned/transactions_cleaned.csv")
transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'])

# Cohort ayı / kullanıcı ilk transaction
transactions['cohort_month'] = transactions.groupby('user_id')['transaction_date'].transform('min').dt.to_period('M')
transactions['tx_month'] = transactions['transaction_date'].dt.to_period('M')

# Cohort dönemleri ve retention hesaplama
cohorts = transactions.groupby(['cohort_month','tx_month'])['user_id'].nunique().reset_index()
cohorts['period_number'] = (cohorts['tx_month'].dt.to_timestamp() - cohorts['cohort_month'].dt.to_timestamp()).dt.days // 30 + 1

cohort_pivot = cohorts.pivot_table(index='cohort_month', columns='period_number', values='user_id')
cohort_pivot.to_csv("../data/cohort_analysis.csv")

