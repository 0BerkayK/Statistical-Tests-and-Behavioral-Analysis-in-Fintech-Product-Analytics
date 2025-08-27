# Weekly Insight Report

## 1. KPI Özetleri
- Total User: 1907
- Total number of transactions: 5997
- Total transaction amount: 165268.56

## 2. Günlük Transaction Trend
- Grafik: `06_summary_report.ipynb` daily_tx lineplot

## 3. A/B Test Sonuçları
| Grup      | Retention 7d |
|-----------|--------------|
| Control   | 0.42         |
| Treatment | 0.37         |
- p-value: 0.12 → istatistiksel olarak anlamlı değil

## 4. Cohort Analizi
- 2023-06 cohort’un 1. ayında retention: 0.35
- 2023-07 cohort’un 1. ayında retention: 0.38


## 6. Anomaly Detection
- Tespit edilen anomaliler: 3 günlük transaction tutarı çok yüksek
- Detaylar: `anomalies_detected.csv`

## 7. Öneriler
- A/B testi daha fazla kullanıcı ile tekrar edilmeli
- Anomaliler kısa sürede kontrol edilmeli
- Feature adoption düşük segmentler için kullanıcı eğitimi veya rehber modüller eklenebilir
