"""
RFM (Recency, Frequency, Monetary) Customer Segmentation & Elasticity Engine
Author: Akash V (@akashvenkey)
"""
import pandas as pd
import numpy as np

def compute_rfm_segments(df):
    """Compute RFM quintile scores and assign segment personas."""
    df['R_Score'] = pd.qcut(df['Recency'], 4, labels=[4, 3, 2, 1])
    df['F_Score'] = pd.qcut(df['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
    df['M_Score'] = pd.qcut(df['Monetary'], 4, labels=[1, 2, 3, 4])
    df['RFM_Sum'] = df['R_Score'].astype(int) + df['F_Score'].astype(int) + df['M_Score'].astype(int)
    
    def assign_tier(score):
        if score >= 10: return "Champions"
        elif score >= 8: return "Loyal Adopters"
        elif score >= 6: return "Needs Attention"
        else: return "At Risk / Hibernating"
        
    df['Segment'] = df['RFM_Sum'].apply(assign_tier)
    return df

if __name__ == "__main__":
    sample_customers = pd.DataFrame({
        'CustomerID': [101, 102, 103, 104, 105],
        'Recency': [5, 45, 12, 180, 25],
        'Frequency': [14, 3, 8, 1, 6],
        'Monetary': [2450.0, 320.5, 1150.0, 85.0, 780.0]
    })
    results = compute_rfm_segments(sample_customers)
    print("=== RFM Customer Segmentation Results ===")
    print(results[['CustomerID', 'RFM_Sum', 'Segment']])