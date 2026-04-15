# Heart Failure Prediction Pipeline

An end-to-end data engineering and machine learning pipeline designed to process clinical records and predict patient mortality risk.

## Architecture

1. Data Ingestion: Loading raw CSV data (based on the Heart Failure Clinical Records 2020 dataset) directly into an SQLite database.
2. Data Transformation (ETL): Utilizing SQL to cast string variables into appropriate numeric data types (REAL and INTEGER), creating a clean Data Mart optimized for machine learning.
3. Machine Learning: Training a Gaussian Naive Bayes classifier (scikit-learn) to predict death events based on 12 clinical features.

## How to Run

1. Clone this repository:
   `bash
   git clone <your_repo_url>
   cd <your_repository_name>

2. Create and activate a virtual environment (recommended):
    python -m venv venv
    # Windows: venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate

3. Install the required dependencies: 
    pip install -r requirements.txt

4. Initialize the database and load the raw data:
    python 01_init_db.py

5. Execute the SQL ETL script to create the ML-ready dataset: 
    python 02_fix_and_check.py

6. Train and evaluate the model: 
    python 03_train_model.py


Results
The initial Gaussian Naive Bayes model demonstrated high Precision (0.91) when identifying critical patients. However, the Recall (0.40) indicates that the model is currently too conservative. Further hyperparameter tuning and feature engineering are required to reduce the False Negative rate for medical deployment.