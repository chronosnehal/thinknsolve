#!/usr/bin/env python3
"""
Pandas Data Analysis and Processing - Solution Implementation

Description: Comprehensive exploratory data analysis on e-commerce sales data using pandas.
Time Complexity: O(n log n) for sorting operations, O(n) for most pandas operations
Space Complexity: O(n) where n is the total number of records across all datasets
"""

import pandas as pd
from typing import Dict
import os

class EcommerceDataAnalyzer:
    """
    E-commerce data analysis engine using pandas.

    Time Complexity: O(n) for loading and basic operations, O(n log n) for sorting/grouping
    Space Complexity: O(n) where n is total records across datasets
    """

    def __init__(self):
        """
        Initialize analyzer with empty dataframes.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.sales_df = None
        self.products_df = None
        self.customers_df = None
        self.merged_df = None

        # Calculate data directory path more efficiently
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(current_dir, '..', '..', 'datasets')

    def load_datasets(self) -> bool:
        """
        Load e-commerce datasets from CSV files.

        Time Complexity: O(n) where n is total rows across all files
        Space Complexity: O(n) for storing dataframes in memory

        Returns:
            bool: True if all datasets loaded successfully, False otherwise
        """
        try:
            print("📊 Loading e-commerce datasets...")

            # Define file paths - O(1)
            file_mapping = {
                'sales': 'online_retail.csv',
                'products': 'products.csv',
                'customers': 'customers.csv'
            }

            # Check file existence - O(1) per file
            for name, filename in file_mapping.items():
                filepath = os.path.join(self.data_dir, filename)
                if not os.path.exists(filepath):
                    print(f"❌ Missing dataset file: {filename}")
                    return False

            # Load datasets - O(n) per file where n is number of rows
            print("  📈 Loading sales transactions...")
            self.sales_df = pd.read_csv(os.path.join(self.data_dir, 'online_retail.csv'))

            print("  📦 Loading product catalog...")
            self.products_df = pd.read_csv(os.path.join(self.data_dir, 'products.csv'))

            print("  👥 Loading customer data...")
            self.customers_df = pd.read_csv(os.path.join(self.data_dir, 'customers.csv'))

            # Basic data transformation - O(n) per operation
            self._transform_data()

            print(f"✅ Successfully loaded datasets:")
            print(f"   📈 Sales: {len(self.sales_df):,} transactions")
            print(f"   📦 Products: {len(self.products_df):,} products")
            print(f"   👥 Customers: {len(self.customers_df):,} customers")

            return True

        except Exception as e:
            print(f"❌ Error loading datasets: {e}")
            return False

    def _transform_data(self) -> None:
        """
        Transform and clean the loaded data for analysis.

        Time Complexity: O(n) for each transformation operation
        Space Complexity: O(1) additional space (in-place operations)
        """
        # Standardize sales data column names - O(1)
        self.sales_df.rename(columns={
            'InvoiceNo': 'transaction_id',
            'StockCode': 'product_code',
            'Quantity': 'quantity',
            'InvoiceDate': 'transaction_date',
            'UnitPrice': 'unit_price',
            'CustomerID': 'customer_id'
        }, inplace=True)

        # Convert date column - O(n)
        self.sales_df['transaction_date'] = pd.to_datetime(self.sales_df['transaction_date'])

        # Remove rows with missing customer IDs - O(n)
        self.sales_df.dropna(subset=['customer_id'], inplace=True)
        self.sales_df['customer_id'] = self.sales_df['customer_id'].astype(int)

        # Standardize products data - O(1)
        self.products_df.rename(columns={
            'StockCode': 'product_code',
            'Description': 'product_name',
            'Category': 'category',
            'UnitPrice': 'price'
        }, inplace=True)

        # Standardize customers data - O(1)
        self.customers_df.rename(columns={
            'CustomerID': 'customer_id',
            'CustomerName': 'customer_name',
            'Country': 'country',
            'Segment': 'segment',
            'Region': 'region',
            'JoinDate': 'join_date'
        }, inplace=True)

        # Convert customer join dates - O(n)
        self.customers_df['join_date'] = pd.to_datetime(self.customers_df['join_date'])

    def clean_data(self) -> Dict:
        """
        Clean and preprocess all datasets.

        Time Complexity: O(n) for each cleaning operation
        Space Complexity: O(1) additional space (mostly in-place operations)

        Returns:
            Dict: Summary of cleaning operations performed
        """
        initial_sales_count = len(self.sales_df)

        # Remove duplicates - O(n log n) for sorting, O(n) for comparison
        duplicates_removed = self.sales_df.duplicated().sum()
        self.sales_df.drop_duplicates(inplace=True)

        # Remove invalid quantities and prices - O(n) per filter
        invalid_quantities = (self.sales_df['quantity'] <= 0).sum()
        self.sales_df = self.sales_df[self.sales_df['quantity'] > 0]

        invalid_prices = (self.sales_df['unit_price'] <= 0).sum()
        self.sales_df = self.sales_df[self.sales_df['unit_price'] > 0]

        # Clean products data - O(n)
        self.products_df['price'] = pd.to_numeric(self.products_df['price'], errors='coerce')
        self.products_df.dropna(subset=['price'], inplace=True)

        return {
            'initial_count': initial_sales_count,
            'final_count': len(self.sales_df),
            'duplicates_removed': duplicates_removed,
            'invalid_quantities_removed': invalid_quantities,
            'invalid_prices_removed': invalid_prices
        }

    def merge_datasets(self) -> bool:
        """
        Merge all datasets for comprehensive analysis.

        Time Complexity: O(n log m) where n,m are sizes of datasets being merged
        Space Complexity: O(n+m) for storing merged result

        Returns:
            bool: True if merge successful, False otherwise
        """
        try:
            # Merge sales with products - O(n log m)
            sales_products = self.sales_df.merge(
                self.products_df,
                on='product_code',
                how='left'
            )

            # Merge with customers - O(n log k)
            self.merged_df = sales_products.merge(
                self.customers_df,
                on='customer_id',
                how='left'
            )

            # Calculate revenue - O(n)
            self.merged_df['revenue'] = (
                self.merged_df['quantity'] * self.merged_df['unit_price']
            )

            # Add time-based columns - O(n)
            self.merged_df['month'] = self.merged_df['transaction_date'].dt.to_period('M')
            self.merged_df['year'] = self.merged_df['transaction_date'].dt.year

            print(f"✅ Merged dataset created with {len(self.merged_df):,} records")
            return True

        except Exception as e:
            print(f"❌ Error merging datasets: {e}")
            return False

    def calculate_business_metrics(self) -> Dict:
        """
        Calculate key business metrics.

        Time Complexity: O(n) for aggregation operations
        Space Complexity: O(1) for storing results

        Returns:
            Dict: Key business metrics
        """
        return {
            'total_revenue': self.merged_df['revenue'].sum(),
            'total_transactions': len(self.merged_df),
            'average_order_value': self.merged_df['revenue'].mean(),
            'unique_customers': self.merged_df['customer_id'].nunique(),
            'unique_products': self.merged_df['product_code'].nunique(),
            'date_range': {
                'start': self.merged_df['transaction_date'].min(),
                'end': self.merged_df['transaction_date'].max()
            }
        }

    def analyze_by_category(self) -> pd.DataFrame:
        """
        Analyze sales performance by product category.

        Time Complexity: O(n log k) where k is number of categories
        Space Complexity: O(k) for storing category results

        Returns:
            pd.DataFrame: Category analysis results
        """
        category_analysis = self.merged_df.groupby('category').agg({
            'revenue': ['sum', 'mean', 'count'],
            'quantity': 'sum',
            'customer_id': 'nunique'
        }).round(2)

        # Flatten column names - O(k)
        category_analysis.columns = [
            'total_revenue', 'avg_revenue', 'transaction_count',
            'total_quantity', 'unique_customers'
        ]

        # Calculate revenue percentage - O(k)
        total_revenue = self.merged_df['revenue'].sum()
        category_analysis['revenue_percentage'] = (
            category_analysis['total_revenue'] / total_revenue * 100
        ).round(1)

        return category_analysis.sort_values('total_revenue', ascending=False)

    def analyze_monthly_trends(self) -> pd.DataFrame:
        """
        Analyze monthly sales trends.

        Time Complexity: O(n log m) where m is number of months
        Space Complexity: O(m) for storing monthly results

        Returns:
            pd.DataFrame: Monthly trend analysis
        """
        monthly_trends = self.merged_df.groupby('month').agg({
            'revenue': 'sum',
            'transaction_id': 'count',
            'customer_id': 'nunique'
        }).round(2)

        monthly_trends.columns = ['revenue', 'transactions', 'unique_customers']

        # Calculate month-over-month growth - O(m)
        monthly_trends['revenue_growth'] = (
            monthly_trends['revenue'].pct_change() * 100
        ).round(1)

        return monthly_trends

    def create_pivot_analysis(self) -> pd.DataFrame:
        """
        Create pivot table for category vs region analysis.

        Time Complexity: O(n) for pivot operation
        Space Complexity: O(k*r) where k=categories, r=regions

        Returns:
            pd.DataFrame: Pivot table results
        """
        return pd.pivot_table(
            self.merged_df,
            values='revenue',
            index='category',
            columns='region',
            aggfunc='sum',
            fill_value=0
        ).round(2)

    def generate_summary_report(self) -> str:
        """
        Generate comprehensive business analysis report.

        Time Complexity: O(n log n) for various aggregations and sorting
        Space Complexity: O(k) where k is number of categories/regions

        Returns:
            str: Formatted analysis report
        """
        if self.merged_df is None:
            return "❌ No data available for analysis"

        report = ["=== E-commerce Sales Analysis Report ===\n"]

        # Business metrics - O(n)
        metrics = self.calculate_business_metrics()
        report.extend([
            "Key Business Metrics:",
            f"- Total Revenue: ${metrics['total_revenue']:,.2f}",
            f"- Average Order Value: ${metrics['average_order_value']:.2f}",
            f"- Total Transactions: {metrics['total_transactions']:,}",
            f"- Unique Customers: {metrics['unique_customers']:,}",
            f"- Unique Products: {metrics['unique_products']:,}",
            f"- Date Range: {metrics['date_range']['start'].strftime('%Y-%m-%d')} to {metrics['date_range']['end'].strftime('%Y-%m-%d')}\n"
        ])

        # Category analysis - O(n log k)
        category_analysis = self.analyze_by_category()
        report.append("Top 3 Categories by Revenue:")
        for i, (category, row) in enumerate(category_analysis.head(3).iterrows(), 1):
            report.append(f"{i}. {category}: ${row['total_revenue']:,.2f} ({row['revenue_percentage']:.1f}%)")

        return "\n".join(report)

def main():
    """
    Main function to demonstrate the pandas data analysis solution.

    Overall Time Complexity: O(n log n) dominated by merge and groupby operations
    Overall Space Complexity: O(n) for storing datasets and merged results
    """
    print("🔍 Starting E-commerce Data Analysis...")

    # Initialize analyzer - O(1)
    analyzer = EcommerceDataAnalyzer()

    try:
        # Load datasets - O(n)
        if not analyzer.load_datasets():
            print("❌ Failed to load datasets")
            return

        # Clean data - O(n)
        print("🧹 Cleaning and preprocessing data...")
        cleaning_report = analyzer.clean_data()
        print(f"✓ Processed {cleaning_report['initial_count']:,} → {cleaning_report['final_count']:,} sales records")

        # Merge datasets - O(n log m)
        print("🔗 Merging datasets...")
        if not analyzer.merge_datasets():
            print("❌ Failed to merge datasets")
            return

        # Generate analysis report - O(n log n)
        print("📈 Generating analysis report...")
        report = analyzer.generate_summary_report()
        print("\n" + report)

        # Show detailed analytics
        print("\n" + "="*50)
        print("📊 Detailed Analytics:")
        print("="*50)

        # Category performance - O(n log k)
        print("\nCategory Performance Analysis:")
        category_df = analyzer.analyze_by_category()
        print(category_df.head().to_string())

        # Monthly trends - O(n log m)
        print("\nMonthly Sales Trends (Last 5 months):")
        monthly_df = analyzer.analyze_monthly_trends()
        print(monthly_df.tail().to_string())

        # Pivot analysis - O(n)
        print("\nRevenue by Category and Region:")
        pivot_df = analyzer.create_pivot_analysis()
        print(pivot_df.to_string())

        print(f"\n✅ Analysis complete! Processed {len(analyzer.merged_df):,} records successfully.")

    except Exception as e:
        print(f"❌ An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
