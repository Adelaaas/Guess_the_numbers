import pyodbc 
import random
import GenerateNumbers

# функция, которая на вход получает кол-во чисел
# и возвращает из базы данных кол-во чисел
def get_numbers(n):
    cnxn = pyodbc.connect(driver='{ODBC Driver 13 for SQL Server}', server='DESKTOP-L39EA60\sqlexpress', database='Numbers',trusted_connection='yes')
    cursor = cnxn.cursor()
    cursor.execute('SELECT top(?) * FROM Numbers', n)
    result =  cursor.fetchall()
    results = []
    for item in result:
        results.append(item[0])

    return results

# print(get_numbers(6))