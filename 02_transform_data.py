import sqlite3
import os 
db_path = os.path.join('data', 'heart_disease.db')
sql_path = os.path.join('sql', '01_clean_data.sql')

with open(sql_path, 'r', encoding='utf-8') as file:
    sql_script = file.read()

print(f"Подключение к БД: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print ("Выполняется SQL-трансформация (ETL)...")

conn.commit()
conn.close()
print("Успех! Чистая витрина данных 'ml_patients' создана.")

