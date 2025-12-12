# Customer Churn Prediction Using Snowflake Feature Engineering

This repository contains my solution for the Snowflake feature engineering assignment.

## Files

- `project_sql.sql`  
  - Creates the Snowflake tables:
    - `RAW_CUSTOMERS`
    - `CLEANED_CUSTOMERS`
    - `CUSTOMER_FEATURES` (feature store table)
    - `TRAIN_CUSTOMERS`, `TEST_CUSTOMERS`
- `churn_rule_scoring.py`  
  - Snowpark Python code that reads `TEST_CUSTOMERS`,
    applies a simple rule-based churn logic using engineered features,
    and writes predictions into `CHURN_PREDICTIONS`.
- `churn_feature_engineering_snowflake.pptx`  
  - Presentation describing:
    - Business problem (customer churn)
    - Snowflake setup and data loading
    - Data cleaning
    - Feature engineering and feature store
    - Train/test split
    - Rule-based prediction step and results.

## How to Reproduce in Snowflake

1. **SQL setup**

   - Open a SQL worksheet and run the statements from `project_sql.sql`.
   - Load the churn CSV into the `RAW_CUSTOMERS` table.
   - Confirm that `CLEANED_CUSTOMERS`, `CUSTOMER_FEATURES`,
     `TRAIN_CUSTOMERS`, and `TEST_CUSTOMERS` are created.

2. **Prediction step (Snowpark Python)**

   - Open a Python worksheet (Snowpark) in Snowflake.
   - Set warehouse and `CUSTOMER_DB.PUBLIC`.
   - Paste the code from `churn_rule_scoring.py` and run it.
   - Check predictions:


