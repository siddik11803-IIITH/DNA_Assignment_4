import sqlite3
import random
from sqlite3.dbapi2 import Cursor
connect = sqlite3.connect('./num.db')
cursor = connect.cursor()
query = '''
    
'''
#type your query here.
cursor.execute(query)
print(str(cursor.fetchall()))