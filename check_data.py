import pandas as pd 
import sqlite3
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'data', 'heart_disease.db')
conn = sqlite3.connect(db_path)
try:
    df = pd.read_sql_query("SELECT * FROM ml_patients LIMIT 5;", conn)
    print("Успех! Таблица ml_patients существует. Вот первые 5 строк:")
    print(df.to_string())
    print("-" * 50)
    print(f"Типы данных в колонках:\n{df.dtypes}")
except Exception as e: 
    print (f"Ошибка: {e}")
finally:
    conn.close() 