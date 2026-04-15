import pandas as pd 
import sqlite3
import os 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report 

print("1. Подключение к БД и выгрузка чистых данных...")
db_path = os.path.join('data', 'heart_disease.db')
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT*FROM ml_patients", conn)
conn.close()

print(f"Данные загружены. Размер: {df.shape}")
print("Подготовка данных для ML...")
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

print ("3. Обучение модели Гауссовского Наивного Байеса...")
model = GaussianNB()

model.fit(X_train, y_train)

print ("4. Тестирование и оценка...")

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"\nОбщая точность (Accuracy): {accuracy*100:.2f}%\n")
print("Детальный отчёт по классам:")
print(classification_report(y_test, predictions))
