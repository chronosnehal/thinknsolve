# Machine Learning Model Training and Evaluation

## Context
In data science and machine learning roles, professionals frequently need to quickly prototype and evaluate classification models on real-world datasets. The ability to efficiently load data, perform feature engineering, train multiple models, and evaluate their performance is fundamental to the ML workflow. This problem simulates a realistic scenario where you need to build and compare classification models to solve a business problem using scikit-learn.

## Problem Statement
Build a Python script that trains and evaluates multiple machine learning models on the Titanic survival dataset using scikit-learn. You'll need to implement a complete ML pipeline including data loading, preprocessing, feature engineering, model training, and performance evaluation.

Your script should:
1. Load the Titanic dataset from CSV file
2. Perform exploratory data analysis and handle missing values
3. Engineer features and prepare data for training
4. Train multiple classification models (Logistic Regression, Decision Tree, Random Forest)
5. Split data into training and testing sets
6. Evaluate model performance using accuracy, precision, recall, and F1-score
7. Compare models and identify the best performer
8. Provide insights on feature importance and model interpretability
9. Handle edge cases and data quality issues gracefully

## Requirements
- Use scikit-learn for all machine learning operations
- Load real Titanic dataset (891 passengers) from datasets directory
- Implement data preprocessing pipeline (missing values, categorical encoding)
- Train at least 3 different classification algorithms
- Use proper train/test split (80/20 or 70/30)
- Calculate comprehensive evaluation metrics (accuracy, precision, recall, F1)
- Provide feature importance analysis
- Handle categorical variables appropriately (one-hot encoding or label encoding)
- Complete execution within 10 seconds for the dataset
- Include cross-validation for robust model evaluation
- Provide clear, formatted output with model comparison
- Include proper error handling and data validation

## Assumptions
- Titanic dataset is available as CSV file in datasets directory
- Dataset contains typical passenger information (age, sex, class, fare, etc.)
- Some missing values exist and need to be handled appropriately
- Python environment has scikit-learn, pandas, and numpy available
- Target variable is binary (survived/not survived)
- Memory constraints allow loading the full dataset
- Output should be interpretable for business stakeholders

## For Examiner

### Difficulty Level
Intermediate

### Expected Time
**MANDATORY**: 35-45 minutes

### Key Concepts Being Tested
- Scikit-learn model training and evaluation
- Data preprocessing and feature engineering
- Train/test split and cross-validation
- Multiple classification algorithms comparison
- Performance metrics calculation and interpretation
- Feature importance analysis
- Missing value handling strategies
- Categorical variable encoding
- Model selection and comparison
- ML pipeline construction

### Hints (if needed)
- Use `pd.read_csv()` for data loading
- Consider `train_test_split()` for data splitting
- Use `SimpleImputer` for missing value handling
- Try `LabelEncoder` or `OneHotEncoder` for categorical variables
- Implement `LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`
- Use `classification_report()` and `confusion_matrix()` for evaluation
- Consider `cross_val_score()` for robust evaluation

### Solution Approach Plan
1. Load and explore the Titanic dataset structure
2. Implement data cleaning and missing value handling
3. Engineer features and encode categorical variables
4. Split data into training and testing sets
5. Train multiple classification models
6. Evaluate each model with comprehensive metrics
7. Compare models and identify best performer
8. Analyze feature importance and provide insights
9. Add proper error handling and validation

## Example Input/Output
```
Input: titanic.csv (891 passengers with features like age, sex, class, fare)
Output:
=== ML Model Training Results ===

Dataset Overview:
- Total Passengers: 891
- Features: 11
- Target: Survived (Binary Classification)
- Missing Values Handled: Age (177), Cabin (687), Embarked (2)

Model Performance Comparison:
1. Random Forest: Accuracy=0.832, Precision=0.789, Recall=0.756, F1=0.772
2. Logistic Regression: Accuracy=0.803, Precision=0.741, Recall=0.733, F1=0.737
3. Decision Tree: Accuracy=0.775, Precision=0.720, Recall=0.689, F1=0.704

Best Model: Random Forest
Top Features: Sex, Fare, Age, Pclass, Family_Size

Cross-Validation Score: 0.826 ± 0.034
```
