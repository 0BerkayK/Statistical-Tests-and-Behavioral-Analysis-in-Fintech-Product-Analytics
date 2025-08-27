# Fintech Ürün Analitiği — İstatistiksel Analiz & Test Odaklı Proje

Bu proje, Sipay benzeri bir fintech ürün veri analisti rolünü simüle etmek amacıyla hazırlanmıştır.
Amaç, kullanıcı davranışlarını ve ürün kullanımını istatistiksel yöntemlerle analiz ederek, A/B testlerini, segment bazlı feature adoption’ı, cohort retention’ı ve anomalileri tespit etmek; sonuçları yönetim raporları şeklinde sunmaktır.

Projede kullanılan veriler simüle edilmiş sentetik verilerdir, ancak gerçek dünya senaryolarına uygun olacak şekilde tasarlanmıştır.

🔹 Proje Adımları

01_data_cleaning.ipynb

Eksik ve hatalı değerlerin kontrolü ve temizlenmesi

Duplicates, outlier ve tip dönüşümleri

02_cohort_retention.ipynb

Kullanıcı cohort’ları oluşturma

D1/D7/D30 retention hesaplamaları ve heatmap görselleştirme

03_ab_test_analysis.ipynb / ab_test.py

Onboarding veya feature A/B testleri

Proportion z-test ile anlamlılık analizi

04_segment_feature_adoption.ipynb

Segment bazlı feature adoption analizi

Chi-square testi

05_anomaly_detection.ipynb / anomaly_alert.py

KPI ve transaction verilerinde olağandışı değerlerin tespiti

Z-score yöntemi ile anomaly detection ve CSV / opsiyonel alert

06_summary_report.ipynb / cohort_calculator.py / weekly_insight_report.md

Tüm analizlerin birleştirilmesi ve görselleştirilmesi

Yönetim için okunabilir weekly insight report üretimi
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
│   │   ├── users_cleaned.csv
│   │   └── transactions_cleaned.csv
│   │   
│   ├── ab_test_data.csv
│   ├── anomalies_detected.csv
│   ├── cohort_analysis.csv
│   ├── feature_adoption.csv
│   ├── user_segment.csv
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
│   ├── generate_segments_adoption.py
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



