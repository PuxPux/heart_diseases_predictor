import pandas as pd
import sqlite3 
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

BASE_DIR = os.getcwd()
db_path = os.path.join(BASE_DIR, 'data', 'heart_disease.db')

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM ml_patients", conn)
conn.close()

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

print(f"Accuracy:{accuracy_score(y_test, predictions)*100:2f}%\n")
print("Detailed report by classes:")
print(classification_report(y_test, predictions))

print("\nThe effect of each clinical indicator on mortality risk (Feature weights):")
coefficients = model.coef_[0]
feature_importance = pd.DataFrame({'Feature': X.columns, 'Weight':coefficients})
feature_importance["Abs_Weight"] = feature_importance['Weight'].abs()
feature_importance = feature_importance.sort_values (by='Abs_Weight', ascending=False)
print(feature_importance[['Feature', 'Weight']].to_string(index=False))