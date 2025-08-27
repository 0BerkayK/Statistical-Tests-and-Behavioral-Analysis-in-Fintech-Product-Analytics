import pandas as pd
import numpy as np
from scipy import stats
import smtplib
from email.message import EmailMessage

transactions = pd.read_csv("../data/cleaned/transactions_cleaned.csv")
transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'])

daily_sum = transactions.groupby('transaction_date')['amount'].sum().reset_index()
daily_sum.rename(columns={'amount':'daily_total'}, inplace=True)

daily_sum['z_score'] = np.abs(stats.zscore(daily_sum['daily_total']))
threshold = 2
daily_sum['is_anomaly'] = daily_sum['z_score'] > threshold

anomalies = daily_sum[daily_sum['is_anomaly']]

# Alert (console log + CSV)
if not anomalies.empty:
    print(f"⚠️ Anomalies detected ({len(anomalies)} rows)")
    anomalies.to_csv("../data/anomalies_detected.csv", index=False)
else:
    print("No anomalies detected.")

SEND_EMAIL = False
if SEND_EMAIL and not anomalies.empty:
    EMAIL_ADDRESS = "email@example.com"
    EMAIL_PASSWORD = "password"
    msg = EmailMessage()
    msg['Subject'] = f"⚠️ Anomaly Alert: {len(anomalies)} detected"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "product_team@example.com"
    msg.set_content(f"Detected anomalies:\n\n{anomalies.to_string(index=False)}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("📧 Email alert sent.")