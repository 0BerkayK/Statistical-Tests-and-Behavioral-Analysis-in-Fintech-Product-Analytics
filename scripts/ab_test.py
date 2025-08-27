import pandas as pd

# Veri yükleme
ab_test = pd.read_csv("../data/ab_test_data.csv")

# Kontrol ve treatment grupları
control = ab_test[ab_test['group'] == 'control']['retained_7d']
treatment = ab_test[ab_test['group'] == 'treatment']['retained_7d']

# Proportion z-test
n_control = len(control)
n_treat = len(treatment)
p1 = control.mean()
p2 = treatment.mean()
p_pool = (control.sum() + treatment.sum()) / (n_control + n_treat)
z = (p1 - p2) / ((p_pool*(1-p_pool)*(1/n_control + 1/n_treat))**0.5)

# p-value
from scipy.stats import norm
p_value = 2 * (1 - norm.cdf(abs(z)))

print(f"z-stat: {z}")
print(f"p-value: {p_value}")
