# Fintech Ürün Analitiği — İstatistiksel Analiz & Test Odaklı Proje

**Kısa özet:** Bu proje Sipay benzeri bir cüzdan/ödeme ürünü senaryosunda istatistiksel analizler ve A/B testleri yapacak şekilde tasarlanmıştır. Hedef, ilanındaki teknik beceriler ve sorumlulukları (cohort, retention, A/B test, segment analizi, anomaly detection, KPI dashboard mantığı) uçtan uca simüle etmektir.

---

## Proje amaçları

* Gerçekçi (veya sentetik) veri ile **istatistiksel A/B testleri**, **cohort-retention analizi**, **segment & feature adoption analizi**, ve **anomaly detection** gerçekleştirmek.
* Her adım için Jupyter notebook + script sağlamak, reproducible ve açıklayıcı sonuçlar üretmek.

---

## Çalışma dizini

```
fintech_product_analysis/
│
├── data/
│   ├── raw/
│   │   ├── users.csv
│   │   └── transactions.csv
│   └── cleaned/
│       ├── users_cleaned.csv
│       └── transactions_cleaned.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_cohort_retention.ipynb
│   ├── 03_ab_test_analysis.ipynb
│   ├── 04_segment_feature_adoption.ipynb
│   ├── 05_anomaly_detection.ipynb
│   └── 06_summary_report.ipynb
│
├── scripts/
│   ├── ab_test.py
│   ├── anomaly_alert.py
│   └── cohort_calculator.py
│
├── reports/
│   └── weekly_insight_report.md
│
├── README.md
└── requirements.txt
```

---

## Çalışma ortamı kurulumu

1. Sanal ortam oluşturun (venv veya conda)
2. `requirements.txt` içeriğini yükleyin:

```
# örnek requirements.txt içeriği
pandas
numpy
matplotlib
seaborn
scipy
statsmodels
jupyter
duckdb
sqlalchemy
google-cloud-bigquery      # opsiyonel, BigQuery ile bağlanmak isterseniz
snowflake-connector-python  # opsiyonel
caas_jupyter_tools          # notebook'ta DataFrame gösterimi (çalışma ortamı için)

# zaman serisi/anomali için
pmdarima

```

> Not: BigQuery/Snowflake kullanacaksanız ilgili client kütüphanelerini ekleyin.

---



