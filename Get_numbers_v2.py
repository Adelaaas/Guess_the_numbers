from sqlalchemy import create_engine
import pandas as pd

# функция, которая на вход получает кол-во чисел
# и возвращает из базы данных кол-во чисел
# функция возвращает список
class GetNumbers:
    def get_numbers(self, n):
        engine = create_engine('mysql+mysqlconnector://arkhipov:Fest2020@104.154.72.248/numbers', echo=False)
        result = pd.read_sql(f'SELECT * FROM numbers1 order by rand() LIMIT {n}', con=engine)
        result = result['numberss'].values.tolist()

        return result

# print(get_numbers(6))