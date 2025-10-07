# Data Analysis and Business Intelligence

## Context
Data analysis and reporting are critical business functions that often require translating natural language requirements into analytical insights, SQL queries, and business reports. This problem demonstrates building an AI-powered system that can interpret data requirements and generate appropriate analytical outputs.

## Problem Statement
Implement a comprehensive data analysis system that leverages LLM capabilities to:
1. Transform natural language descriptions into analytical narratives and insights
2. Generate SQL queries from business requirements and schema descriptions
3. Interpret chart and visualization descriptions into business insights
4. Create structured business reports with actionable recommendations
5. Demonstrate prompt design differences between analytical and creative tasks

## Requirements
- Generate SQL queries from natural language descriptions and database schemas
- Analyze data trends and provide business insights from data descriptions
- Interpret visualization requirements and suggest appropriate chart types
- Create comprehensive business reports with executive summaries
- Handle various data types (numeric, categorical, time-series)
- Provide clear, actionable recommendations in business language
- Support multiple LLM providers with robust error handling
- Maintain separation between different analytical functions

## Assumptions
- No actual database connections required; SQL generation is textual only
- Data points provided are small enough to fit within prompt limits
- Output formats are primarily natural language unless explicitly structured
- LLM responses should be concise, readable, and business-focused
- Input data descriptions are reasonable and contain sufficient context

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
40-50 minutes

### Key Concepts Being Tested
- Business intelligence and data analysis workflows
- SQL query generation from natural language
- Data visualization interpretation and recommendations
- Business report writing and executive communication
- Prompt engineering for analytical vs. creative tasks
- System design with clear role separation

### Hints (if needed)
- Provide domain role context (data analyst, SQL expert, business analyst) in system prompts
- Keep user prompts focused on variable elements (schema, requirements, data descriptions)
- Emphasize clarity and actionability over verbosity in outputs
- Consider how different analytical tasks require different expertise roles

### Solution Approach Plan
1. Implement SQL generation with schema-aware prompting
2. Create data trend analysis with business context interpretation
3. Build visualization interpretation with chart type recommendations
4. Design business report generation with executive summary format
5. Implement proper role-based system prompts for each function
6. Add comprehensive error handling and input validation
7. Provide diverse examples covering different analytical scenarios

## Example Input/Output
```
Input: 
- Schema: "users table (id, name, signup_date, plan_type)"
- Requirement: "Find users who signed up last month with premium plans"

Output: 
- SQL Query: "SELECT * FROM users WHERE signup_date >= '2024-09-01' AND plan_type = 'premium'"
- Business insights and recommendations based on query purpose
```
