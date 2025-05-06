# 📊 Marketing Funnel & Attribution Analysis (E-Commerce Simulation)

This project simulates GA4-style tracking data to analyze the effectiveness of marketing campaigns in an e-commerce setting. It covers funnel performance, attribution modeling, and campaign ROI analysis — aligned with real-world marketing analytics workflows used in retail environments.

---

## 🎯 Objectives

- Analyze user journeys from first touch to conversion
- Identify drop-off points across the marketing funnel
- Apply first-touch and last-touch attribution models
- Measure ROI and conversion rates by marketing channel
- Segment users based on behavior and source



## Dataset Overview
This project uses data from the [Multitouch Attribution Modelling Project on Kaggle.](https://www.kaggle.com/code/hughhuyton/multitouch-attribution-modelling)

- Over 586,000 marketing touchpoints
- 240,000 unique customers
- ~18,000 conversions

Each row represents a touchpoint a user has with a marketing channel prior to converting or exiting, enabling various attribution models to be tested (e.g. last-touch, first touch, linear)

### 📄 Key Features in the Dataset:
- `user_id`: Unique identifier for each user
- `timestamp`: Time of each interaction
- `channel`: Marketing channel (e.g., Email, Paid Search, Organic)
- `conversion`: Boolean indicating whether a conversion occurred
- `conversion_value`: Monetary value of the conversion