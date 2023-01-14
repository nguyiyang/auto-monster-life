import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
 
DB_CONNECTION_STRING = os.environ['DB_CONNECTION_STRING']

def get_farm_list(monster_name):
    conn = psycopg2.connect(DB_CONNECTION_STRING)
    cur = conn.cursor()

    sql = "SELECT name FROM {tab} WHERE expiry != 'Expired' and name !='Farm name'".format(tab=monster_name)

    cur.execute(sql)
    farm_list = cur.fetchall()
    cur.close()

    return farm_list