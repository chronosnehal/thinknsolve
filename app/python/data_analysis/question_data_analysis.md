# Pandas Data Analysis and Processing

## Context
In data science and analytics roles, professionals frequently work with messy, real-world datasets that require cleaning, transformation, and analysis. Pandas is the cornerstone library for data manipulation in Python, and proficiency in data wrangling, aggregation, and joining operations is essential for extracting business insights. This problem simulates a realistic scenario where you need to analyze sales data to provide actionable business intelligence.

## Problem Statement
Build a Python script that performs comprehensive exploratory data analysis (EDA) on e-commerce sales data using Pandas. You'll work with multiple CSV files containing sales transactions, product information, and customer data to generate business insights through data cleaning, aggregation, and visualization.

Your script should:
1. Load and inspect multiple CSV datasets (sales, products, customers)
2. Clean and preprocess data (handle missing values, data types, duplicates)
3. Perform data filtering and transformation operations
4. Execute complex aggregations using group-by operations
5. Create pivot tables for cross-tabular analysis
6. Join/merge datasets to create comprehensive views
7. Generate summary statistics and business insights
8. Handle edge cases and data quality issues gracefully

## Requirements
- Use pandas for all data operations (loading, cleaning, analysis)
- Work with at least 3 related datasets (sales, products, customers)
- Implement data cleaning pipeline (missing values, duplicates, type conversion)
- Perform aggregations: total sales by category, monthly trends, top customers
- Create pivot tables showing sales by product category and region
- Join datasets to enrich analysis with product and customer information
- Calculate key business metrics: average order value, customer lifetime value
- Handle data quality issues and provide summary reports
- Generate insights suitable for business stakeholders
- Complete execution within 15 seconds for datasets up to 10,000 records
- Provide clear, formatted output with proper error handling

## Assumptions
- CSV files are available in a standard format
- Data contains typical e-commerce fields (dates, amounts, IDs, categories)
- Some data quality issues exist (missing values, duplicates, inconsistencies)
- Memory constraints allow loading datasets up to 50MB
- Python environment has pandas and numpy available
- Output should be human-readable for business users

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
**MANDATORY**: 35-45 minutes

### Key Concepts Being Tested
- Pandas DataFrame operations and indexing
- Data cleaning and preprocessing techniques
- Aggregation and group-by operations
- Data joining and merging strategies
- Pivot table creation and analysis
- Data type handling and conversion
- Missing value treatment strategies
- Performance optimization for data operations
- Business insight generation from data
- Error handling in data pipelines

### Hints (if needed)
- Use `pd.read_csv()` with appropriate parameters for loading
- Consider `df.info()`, `df.describe()`, and `df.head()` for initial exploration
- Use `groupby()` with multiple aggregation functions
- Implement `merge()` or `join()` operations for dataset combination
- Create sample data if CSV files are not provided
- Use `pd.pivot_table()` for cross-tabular analysis
- Handle datetime conversions with `pd.to_datetime()`

### Solution Approach Plan
1. Create sample datasets or load provided CSV files
2. Implement data inspection and quality assessment functions
3. Build data cleaning pipeline (missing values, duplicates, types)
4. Create aggregation functions for business metrics
5. Implement pivot table analysis for multi-dimensional views
6. Build dataset joining logic for comprehensive analysis
7. Generate formatted business insights and recommendations
8. Add comprehensive error handling and validation

## Example Input/Output
```
Input: sales.csv, products.csv, customers.csv
Output:
=== E-commerce Sales Analysis Report ===

Dataset Overview:
- Sales Records: 8,547 transactions
- Products: 156 unique items
- Customers: 2,341 active users
- Date Range: 2024-01-01 to 2024-12-31

Data Quality Summary:
✓ Missing values handled (3.2% of records)
✓ Duplicates removed (47 records)
✓ Data types standardized

Key Business Metrics:
- Total Revenue: $2,847,392.50
- Average Order Value: $333.85
- Top Product Category: Electronics (42.3% of sales)
- Best Customer Segment: Premium (avg $892 per order)

Monthly Sales Trend:
Jan 2024: $234,567 (15% growth)
Feb 2024: $289,123 (23% growth)
...

Top 5 Products by Revenue:
1. iPhone 15 Pro: $456,789
2. MacBook Air: $389,234
3. Samsung TV: $298,567
...

Regional Performance:
North: $1,203,456 (42.3%)
South: $987,234 (34.7%)
East: $656,702 (23.0%)

Recommendations:
- Focus marketing on Electronics category
- Expand Premium customer acquisition
- Investigate Q3 sales dip for improvement
```
