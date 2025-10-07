#!/usr/bin/env python3
"""
Machine Learning Model Training and Evaluation - Solution Implementation

Description: Complete ML pipeline for training and evaluating classification models on Titanic dataset.
Time Complexity: O(n log n) for tree-based models, O(n*m*k) for cross-validation where n=samples, m=features, k=folds
Space Complexity: O(n*m) for storing dataset and processed features
"""

import pandas as pd
from typing import Dict
import os
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import warnings
warnings.filterwarnings('ignore')

class MLModelTrainer:
    """
    Machine Learning model trainer for classification tasks.

    Time Complexity: O(n*m*k) for training multiple models with cross-validation
    Space Complexity: O(n*m) for storing dataset and engineered features
    """

    def __init__(self):
        """
        Initialize ML trainer with empty data structures.

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.models = {}
        self.results = {}

        # Calculate dataset path efficiently
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_path = os.path.join(current_dir, '..', '..', 'datasets', 'titanic.csv')

    def load_data(self) -> bool:
        """
        Load Titanic dataset from CSV file.

        Time Complexity: O(n*m) where n=rows, m=columns for reading CSV
        Space Complexity: O(n*m) for storing DataFrame

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            print("📊 Loading Titanic dataset...")

            # Check file existence - O(1)
            if not os.path.exists(self.data_path):
                print(f"❌ Dataset file not found: {self.data_path}")
                return False

            # Load dataset - O(n*m)
            self.data = pd.read_csv(self.data_path)

            print(f"✅ Dataset loaded successfully:")
            print(f"   📈 Passengers: {len(self.data):,}")
            print(f"   📊 Features: {len(self.data.columns)}")
            print(f"   🎯 Target: Survived (Binary Classification)")

            # Display basic info - O(m)
            print(f"\nDataset Info:")
            print(f"   Shape: {self.data.shape}")
            print(f"   Missing Values: {self.data.isnull().sum().sum()}")

            return True

        except Exception as e:
            print(f"❌ Error loading dataset: {e}")
            return False

    def explore_data(self) -> Dict:
        """
        Perform exploratory data analysis.

        Time Complexity: O(n*m) for basic statistics and null counts
        Space Complexity: O(m) for storing summary statistics

        Returns:
            Dict: Summary of data exploration
        """
        print("\n🔍 Exploratory Data Analysis:")

        # Basic statistics - O(n*m)
        survival_rate = self.data['Survived'].mean()
        print(f"   Overall Survival Rate: {survival_rate:.1%}")

        # Missing values analysis - O(n*m)
        missing_values = self.data.isnull().sum()
        missing_columns = missing_values[missing_values > 0]

        print("   Missing Values:")
        for col, count in missing_columns.items():
            percentage = (count / len(self.data)) * 100
            print(f"     {col}: {count} ({percentage:.1f}%)")

        # Feature distribution - O(n)
        print(f"\n   Feature Summary:")
        print(f"     Passenger Classes: {sorted(self.data['Pclass'].unique())}")
        print(f"     Gender Distribution: {dict(self.data['Sex'].value_counts())}")
        print(f"     Age Range: {self.data['Age'].min():.0f}-{self.data['Age'].max():.0f} years")

        return {
            'total_passengers': len(self.data),
            'survival_rate': survival_rate,
            'missing_values': dict(missing_columns),
            'features': len(self.data.columns)
        }

    def preprocess_data(self) -> bool:
        """
        Clean and preprocess the dataset for machine learning.

        Time Complexity: O(n*m) for data cleaning and encoding operations
        Space Complexity: O(n*m) for storing processed features

        Returns:
            bool: True if preprocessing successful, False otherwise
        """
        try:
            print("\n🧹 Preprocessing data...")

            # Create a copy for processing - O(n*m)
            df = self.data.copy()

            # Handle missing values - O(n) per column
            print("   Handling missing values...")

            # Fill missing Age with median - O(n)
            age_median = df['Age'].median()
            df['Age'].fillna(age_median, inplace=True)

            # Fill missing Embarked with mode - O(n)
            embarked_mode = df['Embarked'].mode()[0]
            df['Embarked'].fillna(embarked_mode, inplace=True)

            # Drop Cabin (too many missing values) - O(1)
            df.drop('Cabin', axis=1, inplace=True)

            # Feature Engineering - O(n) per operation
            print("   Engineering features...")

            # Create family size feature - O(n)
            df['Family_Size'] = df['SibSp'] + df['Parch'] + 1

            # Create age groups - O(n)
            df['Age_Group'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100],
                                   labels=['Child', 'Teen', 'Adult', 'Middle', 'Senior'])

            # Create fare groups - O(n)
            df['Fare_Group'] = pd.qcut(df['Fare'], q=4, labels=['Low', 'Medium', 'High', 'Very_High'])

            # Encode categorical variables - O(n) per column
            print("   Encoding categorical variables...")

            # Label encode binary/ordinal features - O(n)
            le_sex = LabelEncoder()
            df['Sex_Encoded'] = le_sex.fit_transform(df['Sex'])

            le_embarked = LabelEncoder()
            df['Embarked_Encoded'] = le_embarked.fit_transform(df['Embarked'])

            # One-hot encode multi-class categorical features - O(n*k) where k is unique values
            age_group_encoded = pd.get_dummies(df['Age_Group'], prefix='Age')
            fare_group_encoded = pd.get_dummies(df['Fare_Group'], prefix='Fare')

            # Combine all features - O(n*m)
            feature_columns = [
                'Pclass', 'Sex_Encoded', 'Age', 'SibSp', 'Parch',
                'Fare', 'Embarked_Encoded', 'Family_Size'
            ]

            # Add encoded categorical features - O(n*k)
            for col in age_group_encoded.columns:
                df[col] = age_group_encoded[col]
                feature_columns.append(col)

            for col in fare_group_encoded.columns:
                df[col] = fare_group_encoded[col]
                feature_columns.append(col)

            # Prepare final feature matrix - O(n*m)
            X = df[feature_columns].copy()
            y = df['Survived']

            # Split data into train/test sets - O(n)
            print("   Splitting data (80/20 train/test)...")
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )

            # Scale features for logistic regression - O(n*m)
            scaler = StandardScaler()
            self.X_train_scaled = scaler.fit_transform(self.X_train)
            self.X_test_scaled = scaler.transform(self.X_test)

            print(f"✅ Preprocessing complete:")
            print(f"   Features: {len(feature_columns)}")
            print(f"   Training samples: {len(self.X_train)}")
            print(f"   Testing samples: {len(self.X_test)}")

            return True

        except Exception as e:
            print(f"❌ Error in preprocessing: {e}")
            return False

    def train_models(self) -> bool:
        """
        Train multiple classification models.

        Time Complexity: O(n*m*log(n)) for tree models, O(n*m*k) for logistic regression
        Space Complexity: O(n*m) for storing model parameters

        Returns:
            bool: True if training successful, False otherwise
        """
        try:
            print("\n🤖 Training machine learning models...")

            # Initialize models with optimized parameters - O(1)
            self.models = {
                'Random Forest': RandomForestClassifier(
                    n_estimators=100,
                    random_state=42,
                    max_depth=10,
                    min_samples_split=5
                ),
                'Logistic Regression': LogisticRegression(
                    random_state=42,
                    max_iter=1000,
                    solver='lbfgs'
                ),
                'Decision Tree': DecisionTreeClassifier(
                    random_state=42,
                    max_depth=8,
                    min_samples_split=10
                )
            }

            # Train each model - O(n*m*log(n)) per model
            for name, model in self.models.items():
                print(f"   Training {name}...")

                if name == 'Logistic Regression':
                    # Use scaled features for logistic regression - O(n*m*k)
                    model.fit(self.X_train_scaled, self.y_train)
                else:
                    # Use original features for tree-based models - O(n*m*log(n))
                    model.fit(self.X_train, self.y_train)

            print("✅ All models trained successfully!")
            return True

        except Exception as e:
            print(f"❌ Error training models: {e}")
            return False

    def evaluate_models(self) -> Dict:
        """
        Evaluate all trained models and compare performance.

        Time Complexity: O(n*m) for predictions, O(k*n*m) for cross-validation
        Space Complexity: O(n) for storing predictions

        Returns:
            Dict: Evaluation results for all models
        """
        print("\n📊 Evaluating model performance...")

        self.results = {}

        # Evaluate each model - O(n*m) per model
        for name, model in self.models.items():
            print(f"   Evaluating {name}...")

            # Make predictions - O(n*m)
            if name == 'Logistic Regression':
                y_pred = model.predict(self.X_test_scaled)
                # Cross-validation with scaled features - O(k*n*m)
                cv_scores = cross_val_score(model, self.X_train_scaled, self.y_train, cv=5)
            else:
                y_pred = model.predict(self.X_test)
                # Cross-validation with original features - O(k*n*m)
                cv_scores = cross_val_score(model, self.X_train, self.y_train, cv=5)

            # Calculate metrics - O(n)
            accuracy = accuracy_score(self.y_test, y_pred)
            precision = precision_score(self.y_test, y_pred)
            recall = recall_score(self.y_test, y_pred)
            f1 = f1_score(self.y_test, y_pred)

            # Store results - O(1)
            self.results[name] = {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'predictions': y_pred
            }

        return self.results

    def get_feature_importance(self) -> Dict:
        """
        Extract feature importance from tree-based models.

        Time Complexity: O(m) where m is number of features
        Space Complexity: O(m) for storing importance scores

        Returns:
            Dict: Feature importance for applicable models
        """
        importance_data = {}
        feature_names = self.X_train.columns.tolist()

        # Get importance from tree-based models - O(m)
        for name, model in self.models.items():
            if hasattr(model, 'feature_importances_'):
                importance_scores = model.feature_importances_

                # Sort features by importance - O(m log m)
                feature_importance = list(zip(feature_names, importance_scores))
                feature_importance.sort(key=lambda x: x[1], reverse=True)

                importance_data[name] = feature_importance[:5]  # Top 5 features

        return importance_data

    def generate_report(self) -> str:
        """
        Generate comprehensive model evaluation report.

        Time Complexity: O(m) for feature importance analysis
        Space Complexity: O(k) where k is number of models

        Returns:
            str: Formatted evaluation report
        """
        if not self.results:
            return "❌ No evaluation results available"

        report = ["=== ML Model Training Results ===\n"]

        # Dataset overview - O(1)
        exploration = self.explore_data()
        report.extend([
            "Dataset Overview:",
            f"- Total Passengers: {exploration['total_passengers']:,}",
            f"- Features Used: {len(self.X_train.columns)}",
            f"- Target: Survived (Binary Classification)",
            f"- Survival Rate: {exploration['survival_rate']:.1%}",
            f"- Train/Test Split: {len(self.X_train)}/{len(self.X_test)}\n"
        ])

        # Model performance comparison - O(k)
        report.append("Model Performance Comparison:")
        sorted_models = sorted(self.results.items(), key=lambda x: x[1]['accuracy'], reverse=True)

        for i, (name, metrics) in enumerate(sorted_models, 1):
            report.append(
                f"{i}. {name}: Accuracy={metrics['accuracy']:.3f}, "
                f"Precision={metrics['precision']:.3f}, Recall={metrics['recall']:.3f}, "
                f"F1={metrics['f1_score']:.3f}"
            )

        # Best model identification - O(1)
        best_model_name = sorted_models[0][0]
        best_metrics = sorted_models[0][1]
        report.extend([
            f"\nBest Model: {best_model_name}",
            f"Cross-Validation Score: {best_metrics['cv_mean']:.3f} ± {best_metrics['cv_std']:.3f}"
        ])

        # Feature importance - O(m)
        importance_data = self.get_feature_importance()
        if importance_data:
            report.append(f"\nTop Features ({best_model_name}):")
            if best_model_name in importance_data:
                for feature, importance in importance_data[best_model_name]:
                    report.append(f"  {feature}: {importance:.3f}")

        return "\n".join(report)

def main():
    """
    Main function to demonstrate ML model training and evaluation.

    Overall Time Complexity: O(n*m*log(n)) dominated by model training
    Overall Space Complexity: O(n*m) for storing dataset and features
    """
    print("🤖 Starting ML Model Training Pipeline...")

    # Initialize trainer - O(1)
    trainer = MLModelTrainer()

    try:
        # Load dataset - O(n*m)
        if not trainer.load_data():
            print("❌ Failed to load dataset")
            return

        # Explore data - O(n*m)
        trainer.explore_data()

        # Preprocess data - O(n*m)
        if not trainer.preprocess_data():
            print("❌ Failed to preprocess data")
            return

        # Train models - O(n*m*log(n))
        if not trainer.train_models():
            print("❌ Failed to train models")
            return

        # Evaluate models - O(k*n*m)
        results = trainer.evaluate_models()

        # Generate and display report - O(m)
        print("\n" + trainer.generate_report())

        # Detailed performance analysis
        print("\n" + "="*60)
        print("📈 Detailed Model Analysis:")
        print("="*60)

        for name, metrics in results.items():
            print(f"\n{name} Performance:")
            print(f"  Accuracy: {metrics['accuracy']:.3f}")
            print(f"  Precision: {metrics['precision']:.3f}")
            print(f"  Recall: {metrics['recall']:.3f}")
            print(f"  F1-Score: {metrics['f1_score']:.3f}")
            print(f"  CV Score: {metrics['cv_mean']:.3f} ± {metrics['cv_std']:.3f}")

        print(f"\n✅ ML pipeline complete! Trained and evaluated {len(results)} models successfully.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
