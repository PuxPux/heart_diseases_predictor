#!/bin/bash

echo "=== STARTING ML PIPELINE ==="

echo "-> Step 1: Initializing Database"
python 01_init_db.py

echo "-> Step 2: Running SQL ETL"
python 02_fix_and_check.py

echo "-> Step 3: Training Naive Bayes Model"
python 03_train_model.py

echo "-> Step 4: Training Logistic Regression Model"
python 04_logistic_regression.py

echo "=== PIPELINE FINISHED ==="