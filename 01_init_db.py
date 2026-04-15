# # import pandas as pd 
# # import sqlite3
# # import os

# # csv_filename = 'Heart_failure_clinical_records_dataset.csv'
# # csv_path = os.path.join('data', csv_filename)
# # db_path = os.path.join('data', 'heart_disease.db')

# # print("Start Script")

# # print(f"Search File: {csv_path}")
# # df = pd.read_csv(csv_path, dtype=str)
# # print (f"The File has been successfully read! Strings found: {len(df)}")

# # print ("Create Data Base SQLite3")
# # conn=sqlite3.connect(db_path)

# # df.to_sql('raw_patients', conn, if_exists='replace', index=False)
# # conn.close()

# # print(f"Success! Data Base is ready and saved: {db_path}")



# import pandas as pd 
# import sqlite3 
# import os 

# BASE_DIR = os.getcwd()
# csv_path = os.path.join(BASE_DIR, 'data', 'Heart_failure_clinical_records_dataset.csv')
# db_path = os.path.join(BASE_DIR, 'data', 'heart_disease.db')

# print ("Start Script")
# print (f"Search File: {csv_path}")
# df = pd.read_csv(csv_path)
# print(f"The File has been successfully read! Strings found: {len(df)}")
# print("Create Data Base SQLite3")
# conn = sqlite3.connect(db_path)
# df.to_sql('raw_patients', conn, if_exists='replace', index=False)
# conn.close()
# print(f"Success! Data Base is ready and saved: {db_path}")


import pandas as pd # Подключаем библиотеку pandas для чтения CSV-таблиц
import sqlite3 # Подключаем библиотеку sqlite3 для работы с базами данных
import os # Подключаем библиотеку os для построения правильных путей

BASE_DIR = os.getcwd() # Сохраняем абсолютный путь к папке твоего проекта
csv_path = os.path.join(BASE_DIR, 'data', 'Heart_failure_clinical_records_dataset.csv') # Путь к исходному CSV
db_path = os.path.join(BASE_DIR, 'data', 'heart_disease.db') # Путь к файлу базы данных

print("Start Script") # Печатаем сообщение о старте
print(f"Search File: {csv_path}") # Печатаем путь, где ищем файл

df = pd.read_csv(csv_path) # Читаем ВСЕ 299 строк из CSV в оперативную память
print(f"The File has been successfully read! Strings found: {len(df)}") # Печатаем количество найденных строк

print("Create Data Base SQLite3") # Печатаем сообщение о старте записи
conn = sqlite3.connect(db_path) # Подключаемся к базе (или создаем её)

# КРИТИЧЕСКАЯ СТРОКА: записываем всю таблицу df (299 строк) в базу.
df.to_sql('raw_patients', conn, if_exists='replace', index=False) # if_exists='replace' полностью удалит старую таблицу из 10 строк и запишет новую полную

conn.close() # Закрываем соединение с файлом
print(f"Success! Data Base is ready and saved: {db_path}") # Выводим финальное сообщение с правильным словом ready