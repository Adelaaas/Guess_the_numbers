import pyodbc 
import random

def generate_nembers():
    # подключение к базе данных
    cnxn = pyodbc.connect(driver='{ODBC Driver 13 for SQL Server}', server='DESKTOP-L39EA60\sqlexpress', database='Numbers',trusted_connection='yes')
    cursor = cnxn.cursor()
    
    # цикл, который генерирует 10 000 числе и записывает их в бд
    for i in range(10000):
        n = random.randint(100000,999999)
        cursor.execute('INSERT INTO numbers(number) VALUES (?)', n)
        cnxn.commit() 


