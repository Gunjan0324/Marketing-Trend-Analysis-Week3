"""
Week 3 - Trend Analysis and Insights Generation
Reproducible analysis for the cleaned Week 1 marketing dataset.

Important:
- The dataset has no reliable date/reporting-period column.
- Therefore this script does NOT invent monthly/weekly trends.
- Spend is converted to INR at a fixed presentation rate of 85 INR/USD.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr, kruskal, mannwhitneyu

INPUT = "cleaned_marketing_campaign_data.csv"
FX = 85

df = pd.read_csv(INPUT)

# Why: make business metrics easier to read in the report.
df["Spend_INR"] = df["Spent"] * FX
df["CPA_INR"] = np.where(
    df["Approved_Conversion"] > 0,
    df["Spend_INR"] / df["Approved_Conversion"],
    np.nan
)

# Why: aggregate ad-level records so campaign comparisons are not dominated
# by individual observations.
campaign = df.groupby("xyz_campaign_id").agg(
    Ads=("ad_id","count"),
    Impressions=("Impressions","sum"),
    Clicks=("Clicks","sum"),
    Spend_INR=("Spend_INR","sum"),
    Total_Conversion=("Total_Conversion","sum"),
    Approved_Conversion=("Approved_Conversion","sum")
).reset_index()

campaign["CTR_%"] = campaign["Clicks"] / campaign["Impressions"] * 100
campaign["Approved_CVR_%"] = campaign["Approved_Conversion"] / campaign["Clicks"] * 100
campaign["CPA_INR"] = campaign["Spend_INR"] / campaign["Approved_Conversion"]

# Why: descriptive audience analysis helps identify segments that may deserve
# further targeting or creative tests.
age = df.groupby("age").agg(
    Ads=("ad_id","count"),
    Impressions=("Impressions","sum"),
    Clicks=("Clicks","sum"),
    Spend_INR=("Spend_INR","sum"),
    Approved_Conversion=("Approved_Conversion","sum")
).reset_index()

gender = df.groupby("gender").agg(
    Ads=("ad_id","count"),
    Impressions=("Impressions","sum"),
    Clicks=("Clicks","sum"),
    Spend_INR=("Spend_INR","sum"),
    Approved_Conversion=("Approved_Conversion","sum")
).reset_index()

# Why: Pearson measures linear association; Spearman provides a rank-based
# alternative that is less dependent on normality.
pairs = [
    ("Impressions","Clicks"),
    ("Clicks","Approved_Conversion"),
    ("Spent","Approved_Conversion"),
    ("Spent","Clicks"),
    ("CTR (%)","Approved_Conversion"),
    ("Conversion Rate (%)","Approved_Conversion"),
]

for a, b in pairs:
    m = df[a].notna() & df[b].notna()
    pearson_r, pearson_p = pearsonr(df.loc[m,a], df.loc[m,b])
    spearman_rho, spearman_p = spearmanr(df.loc[m,a], df.loc[m,b])
    print(a, b, pearson_r, pearson_p, spearman_rho, spearman_p)

# Why: Kruskal-Wallis compares 3+ independent groups without requiring
# normally distributed observations.
groups = [g["Approved_Conversion"].values for _, g in df.groupby("xyz_campaign_id")]
print("Kruskal-Wallis:", kruskal(*groups))

# Why: Mann-Whitney U compares two independent distributions without
# assuming normality.
male = df.loc[(df["gender"] == "M") & df["CPA_INR"].notna(), "CPA_INR"]
female = df.loc[(df["gender"] == "F") & df["CPA_INR"].notna(), "CPA_INR"]
print("Mann-Whitney U:", mannwhitneyu(male, female, alternative="two-sided"))

# Why: IQR is a simple robust screening method for unusually high observations.
q1, q3 = df["Spent"].quantile([0.25, 0.75])
upper_spend = q3 + 1.5 * (q3-q1)
print("Spend outliers:", (df["Spent"] > upper_spend).sum())

print("\nImportant interpretation rule:")
print("Correlation is association, not causation. Outliers are reviewed, not automatically deleted.")
