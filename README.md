# Marketing Trend Analysis — Week 3

A complete Week 3 marketing analytics project focused on trend analysis,
exploratory data analysis (EDA), statistical testing, correlation analysis,
anomaly detection, visual insights, and actionable recommendations.

## 📌 Project Overview

This project was completed as part of a marketing analytics
training/internship workflow.

The objective was to move beyond basic data cleaning and visualization
and answer practical marketing questions.

## 📂 Repository Structure

Marketing-Trend-Analysis-Week3/
│
├── Week_3_Trend_Analysis_and_Insights_Report_Futuristic.docx
├── Week_3_Trend_Analysis_Supporting_Analysis.xlsx
├── week3_trend_analysis.py
├── cleaned_marketing_campaign_data.csv
├── requirements.txt
├── README.md
│
└── visualizations/

## 📊 Dataset

The project uses the cleaned marketing campaign dataset prepared
during Week 1.

Key fields include:

- Campaign identifiers
- Age group
- Gender
- Interest
- Impressions
- Clicks
- Spend
- Total conversions
- Approved conversions
- CTR
- CPC
- CPM
- Conversion rate
- CPA
- Spend in INR

The cleaned dataset contains 916 records.

## 🔎 Analysis Performed

### 1. Exploratory Data Analysis

- Campaign scale
- Approved conversion volume
- CPA
- CTR
- Approved conversion rate
- Spend versus conversions
- Age-group performance
- Gender performance
- Interest-level conversion patterns

### 2. Correlation Analysis

Both Pearson and Spearman correlation methods
are used to examine relationships between marketing metrics.

### 3. Statistical Testing

The project applies:

- Kruskal–Wallis test
- Mann–Whitney U test

### 4. Outlier Analysis

The IQR method is used to identify unusually high
or low spend observations.

## 📈 Visualizations

The project includes 12 visualizations covering:

1. Campaign approved conversions
2. Campaign CPA
3. Campaign CTR
4. Campaign approved conversion rate
5. Campaign spend versus conversions
6. Age-group approved conversions
7. Age-group CTR
8. Gender CPA
9. Top interests by conversions
10. Campaign CTR versus CPA
11. Correlation matrix
12. Spend outlier analysis

## 💡 Key Analytical Themes

- Balancing scale and efficiency
- Identifying campaign-level performance differences
- Understanding audience behaviour
- Connecting engagement metrics with conversion outcomes
- Detecting unusual observations
- Using statistical evidence
- Converting findings into practical marketing actions

## ⚠️ Important Limitations

### No time/date field

The dataset does not contain a usable date or reporting-period
column. Therefore, genuine daily, weekly, monthly, yearly,
or seasonal trends cannot be calculated.

No artificial dates were added.

### No revenue/profit field

The dataset contains spend and conversion information but does
not provide reliable revenue or profit.

Therefore, the project does not claim ROI or ROAS.

CPA and conversion-based measures are used instead.

### Association is not causation

Correlation does not prove that one marketing variable causes another.

## 🧪 Reproducibility

Install dependencies:

pip install -r requirements.txt

Run the analysis:

python week3_trend_analysis.py

## 🎯 Outcome

Real Dataset
→ Data Preparation
→ EDA
→ Statistical Analysis
→ Correlation
→ Outlier Detection
→ Visualization
→ Insights
→ Recommendations
