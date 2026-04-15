import pandas as pd 
import sqlite3
import os

csv_filename = 'Heart_failure_clinical_records_dataset.csv'
csv_path = os.path.join('data', csv_filename)
db_path = os.path.join('data', 'heart_disease.db')

print("Start Script")

print(f"Search File: {csv_path}")
df = pd.read_csv(csv_path, dtype=str)
print (f"The File has been successfully read! Strings found: {len(df)}")

print ("Create Data Base SQLite3")
conn=sqlite3.connect(db_path)

df.to_sql('raw_patients', conn, if_exists='replace', index=False)
conn.close()

print(f"Success! Data Base is ready and saved: {db_path}")



