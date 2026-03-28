Telco Customer Churn Prediction – Machine Learning Project


Project Overview

This project aims to predict customer attrition (churn) for a telecommunications company. Retaining existing customers is more cost-effective than acquiring new ones, making churn prediction a critical business task.

By analyzing customer behavior, demographics, and service usage, I built a predictive model that identifies users at high risk of leaving the service.


Dataset

The dataset used in this project is the Telco Customer Churn dataset from Kaggle.
  - Size: 7,043 rows, 21 columns.
  - Target Variable: Churn (Yes/No).
  - Key Features: Tenure, Monthly Charges, Contract Type, Payment Method, and Internet Service.


Tech Stack

- Language: Python 3.10
- Data Manipulation: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Machine Learning: Scikit-Learn (Random Forest, Logistic Regression)


Project Workflow

1. Data Cleaning: Handled missing values in TotalCharges and removed unnecessary identifiers.
2. Exploratory Data Analysis (EDA): Visualized correlations between contract types and churn rates.
3. Feature Engineering: Applied One-Hot Encoding to convert categorical text data into numerical format.
4. Modeling: Split data into training (80%) and testing (20%) sets. Trained a Random Forest Classifier.
5. Evaluation: Measured performance using Accuracy, Precision, Recall, and F1-Score.


Key Insights & Results

- Model Accuracy: 79% on the test set.
- Main Churn Drivers:
  1. Total Charges & Monthly Charges: Higher bills strongly correlate with higher churn.
  2. Tenure: New customers (first 6 months) are significantly more likely to leave.
  3. Contract Type: "Month-to-month" customers have a much higher churn rate compared to those on 1 or 2-year contracts.
  4. Fiber Optic Users: This group showed a surprisingly high churn rate, suggesting potential service dissatisfaction or aggressive competitor pricing.


How to Run

1. Clone this repository.

2. Ensure you have the required libraries installed:

"pip install pandas matplotlib seaborn scikit-learn"

3. Open churn_analysis.ipynb in VS Code or Jupyter Notebook and run all cells.
