import pandas as pd
import numpy as np

np.random.seed(42)

user_ids = range(100000, 102000)

# Segments
segments = ["new_investor", "active_trader", "long_term"]
user_segments = pd.DataFrame({
    "user_id": user_ids,
    "segment": np.random.choice(segments, size=len(user_ids), p=[0.4, 0.3, 0.3])
})
user_segments.to_csv("../data/user_segments.csv", index=False)

# Features
features = ["advanced_chart", "auto_invest", "news_feed"]
rows = []
for user in user_ids:
    for feature in features:
        rows.append({
            "user_id": user,
            "feature_name": feature,
            "adopted": np.random.choice([0, 1], p=[0.6, 0.4])  # %40 adoption
        })
feature_adoption = pd.DataFrame(rows)
feature_adoption.to_csv("../data/feature_adoption.csv", index=False)
