#!/usr/bin/env python3
"""
Data Analysis and SQL Generation - Solution Implementation

Description: A comprehensive data analysis system that transforms natural language into
analytical insights, SQL queries, chart interpretations, and business reports.
"""

from typing import List, Dict, Any

# For GenAI problems ONLY - import LLM client
from app.utils.config import LLMClientManager

def analyze_data_trends(data_description: str, data_points: List[Any] = None, provider: str = "openrouter") -> str:
    """
    Analyze data trends and provide insights.

    Args:
        data_description: Description of the data
        data_points: Optional actual data points
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Data analysis and insights
    """
    client = LLMClientManager.create_client(provider)

    data_context = f"Data description: {data_description}"
    if data_points:
        data_context += f"\nData points: {data_points}"

    messages = [
        {
            "role": "system",
            "content": "You are a data analyst. Analyze the provided data and identify trends, patterns, anomalies, and actionable insights. Provide clear explanations and recommendations."
        },
        {
            "role": "user",
            "content": f"Analyze this data:\n\n{data_context}"
        }
    ]

    return client.chat(messages)

def generate_sql_query(question: str, table_schema: str, provider: str = "openrouter") -> str:
    """
    Generate SQL queries from natural language questions.

    Args:
        question: Natural language question about data
        table_schema: Database schema description
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Generated SQL query
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a SQL expert. Generate efficient, well-formatted SQL queries based on the requirements. Include comments and explain the query logic."
        },
        {
            "role": "user",
            "content": f"Table/Schema description:\n{table_schema}\n\nQuery requirement:\n{question}"
        }
    ]

    return client.chat(messages)

def interpret_chart_data(chart_type: str, chart_description: str, provider: str = "openrouter") -> str:
    """
    Interpret and explain chart data and visualizations.

    Args:
        chart_type: Type of chart (bar, line, pie, scatter, etc.)
        chart_description: Description of the chart data and values
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Chart interpretation and insights
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a data visualization expert. Interpret charts and graphs, explaining what the data shows, key trends, and actionable insights."
        },
        {
            "role": "user",
            "content": f"Chart type: {chart_type}\n\nChart description:\n{chart_description}"
        }
    ]

    return client.chat(messages)

def create_data_report(data_summary: str, business_context: str, provider: str = "openrouter") -> str:
    """
    Create a comprehensive data report with recommendations.

    Args:
        data_summary: Summary of the data analysis
        business_context: Business context and objectives
        provider: LLM provider ("openai", "openrouter")

    Returns:
        Formatted data report
    """
    client = LLMClientManager.create_client(provider)

    messages = [
        {
            "role": "system",
            "content": "You are a business analyst. Create professional data reports with executive summary, key findings, insights, and actionable recommendations."
        },
        {
            "role": "user",
            "content": f"Business context:\n{business_context}\n\nData summary:\n{data_summary}\n\nCreate a comprehensive report."
        }
    ]

    return client.chat(messages)

def main():
    """Main function to demonstrate the solution"""
    try:
        print("=== Data Analysis and SQL Generation System ===\n")

        # Analyze sales data trends
        sales_data = [1200, 1350, 1100, 1500, 1800, 2100, 1900, 2300, 2500, 2200, 2800, 3100]
        data_desc = "Monthly sales figures for the past 12 months (in thousands USD)"

        print("Analyzing sales data trends...")
        analysis = analyze_data_trends(data_desc, sales_data, "openrouter")
        print("Sales Data Analysis:")
        print(analysis)
        print("\n" + "="*50 + "\n")

        # Generate SQL query
        schema = """
        Tables:
        - customers (id, name, email, registration_date, country)
        - orders (id, customer_id, order_date, total_amount, status)
        - products (id, name, category, price)
        - order_items (order_id, product_id, quantity, unit_price)
        """

        requirement = "Find the top 5 customers by total purchase amount in the last 6 months"

        print("Generating SQL query...")
        sql_query = generate_sql_query(requirement, schema)
        print("Generated SQL Query:")
        print(sql_query)
        print("\n" + "="*50 + "\n")

        # Interpret chart data
        chart_desc = "Bar chart showing quarterly revenue: Q1: $2.5M, Q2: $3.1M, Q3: $2.8M, Q4: $3.7M"

        print("Interpreting chart data...")
        chart_interpretation = interpret_chart_data("bar", chart_desc)
        print("Chart Interpretation:")
        print(chart_interpretation)
        print("\n" + "="*50 + "\n")

        # Create business report
        business_context = "E-commerce company looking to optimize customer retention and increase average order value"
        data_summary = "Customer analysis shows 65% retention rate, $85 average order value, peak sales in Q4"

        print("Creating business report...")
        report = create_data_report(data_summary, business_context)
        print("Business Report:")
        print(report)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
