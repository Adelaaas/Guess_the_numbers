import pandas
from sqlalchemy import create_engine
import numpy
import random

def generate_nembers():
    engine = create_engine('mysql+mysqlconnector://arkhipov:Fest2020@104.154.72.248/numbers', echo=False)

    a = numpy.random.randint(100000,999999, size = (10000,1))
    
    df = pandas.DataFrame({'numberss':a[:,0]})
    print(df)
    df.to_sql(con=engine, schema='numbers', name='numbers1', if_exists='replace')