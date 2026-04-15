#!/bin/bash # Указываем операционной системе, что это скрипт для оболочки bash

echo "=== STARTING ML PIPELINE ===" # Выводим в консоль заголовок начала работы

echo "-> Step 1: Initializing Database" # Печатаем текст о старте первого шага
python 01_init_db.py # Запускаем скрипт загрузки всех 299 строк из CSV в базу

echo "-> Step 2: Running SQL ETL" # Печатаем текст о старте второго шага
python 02_fix_and_check.py # Запускаем SQL-трансформацию и создаем витрину ml_patients

echo "-> Step 3: Training Naive Bayes" # Печатаем текст о старте обучения Байеса
python 03_train_model.py # Обучаем и тестируем Наивного Байеса

echo "-> Step 4: Training Logistic Regression" # Печатаем текст о старте Логистической регрессии
python 04_logistic_regression.py # Обучаем регрессию и выводим веса признаков

echo "-> Step 5: Training Random Forest" # Печатаем текст о старте Случайного Леса
python 05_random_forest.py # Обучаем 100 деревьев решений и выводим их метрики

echo "=== PIPELINE FINISHED ===" # Печатаем текст об успешном окончании всех процессов