import sqlite3
import pandas as pd
import os

# Use os.getcwd() to get actual terminal path
BASE_DIR = os.getcwd()
db_path = os.path.join(BASE_DIR, 'data', 'heart_disease.db')

print(f"1. Connect to Data Base: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Chech for the raw csv
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='raw_patients'")
    if cursor.fetchone()[0] == 0:
        print("\n[CRITICAL ERROR]: There is no raw_patients tablet in this Database!")
        print(f"Search path: {db_path}")
    else:
        print("2. Raw Tablet raw_patients has been found. Run SQL-transformation...")
        
        sql_script = """
        DROP TABLE IF EXISTS ml_patients;
        CREATE TABLE ml_patients AS
        SELECT 
            CAST(age AS REAL) AS age,
            CAST(anaemia AS INTEGER) AS anaemia,
            CAST(creatinine_phosphokinase AS INTEGER) AS cpk,
            CAST(diabetes AS INTEGER) AS diabetes,
            CAST(ejection_fraction AS INTEGER) AS ejection_fraction,
            CAST(high_blood_pressure AS INTEGER) AS high_bp,
            CAST(platelets AS REAL) AS platelets,
            CAST(serum_creatinine AS REAL) AS serum_creatinine,
            CAST(serum_sodium AS INTEGER) AS serum_sodium,
            CAST(sex AS INTEGER) AS sex,
            CAST(smoking AS INTEGER) AS smoking,
            CAST(time AS INTEGER) AS days_followed,
            CAST("DEATH_EVENT" AS INTEGER) AS target
        FROM raw_patients;
        """
        
        try:
            cursor.executescript(sql_script)
            conn.commit()
            print("3. [УСПЕХ]: The ml_patients tablet has been successfully created!\n")
            
            df = pd.read_sql_query("SELECT * FROM ml_patients LIMIT 5;", conn)
            print("First 5 strings from new tablet:")
            print("-" * 60)
            print(df.to_string())
            print("-" * 60)
            
        except sqlite3.OperationalError as e:
            print(f"\n[ОШИБКА SQL]: {e}")
            df_raw = pd.read_sql_query("SELECT * FROM raw_patients LIMIT 1;", conn)
            print(f"\nРеальные колонки в твоем CSV файле:\n{list(df_raw.columns)}")
            
except Exception as e:
    print(f"\n[СИСТЕМНАЯ ОШИБКА]: {e}")
finally:
    if 'conn' in locals():
        conn.close()