import pandas as pd
import sqlite3
import os 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

BASE_DIR = os.getcwd()
db_path = os.path.join(BASE_DIR, 'data', 'heart_disease.db')

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM ml_patients", conn)
conn.close()

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, predictions)*100:.2f}%\n")
print("Detailed class report:")
print(classification_report(y_test, predictions))

print("\nFeature imoportance:")
importances = model.feature_importances_
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)
print(feature_importance.to_string(index=False))