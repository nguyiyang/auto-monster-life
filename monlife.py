import gspread
from oauth2client.service_account import ServiceAccountCredentials
import mysql.connector
from mysql.connector.constants import ClientFlag
import os

def create_keyfile_dict():
        variables_keys = {
            "type": os.environ["SHEET_TYPE"],
            "project_id": os.environ["SHEET_PROJECT_ID"],
            "private_key_id": os.environ["SHEET_PRIVATE_KEY_ID"],
            "private_key": os.environ["SHEET_PRIVATE_KEY"],
            "client_email": os.environ["SHEET_CLIENT_EMAIL"],
            "client_id": os.environ["SHEET_CLIENT_ID"],
            "auth_uri": os.environ["SHEET_AUTH_URI"],
            "token_uri": os.environ["SHEET_TOKEN_URI"],
            "auth_provider_x509_cert_url": os.environ["SHEET_AUTH_PROVIDER_X509_CERT_URL"],
            "client_x509_cert_url": os.environ["SHEET_CLIENT_X509_CERT_URL"]
        }
        return variables_keys
  
if __name__ == '__main__':

    PASSWORD_STRING = os.environ['PASSWORD_STRING']
    HOST_STRING = os.environ['HOST_STRING']

    
    # fetches data from the sheets
    # define the scope
    scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name(create_keyfile_dict(), scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)

    sheet = client.open_by_key('1um4UKZcYwRwRSjQh8i_5ujsJEt9AtDiR5nIZsD_9JtY')
    sheet_instance = sheet.worksheet("Elite Bloodfang")
    monster_name = sheet_instance.title
    monster_name = monster_name.replace(' ', '_')
    monster_name = monster_name.lower()
    data = sheet_instance.get_all_values()

    config = {
        'user': 'root',
        'password': PASSWORD_STRING,
        'host': HOST_STRING,
        'client_flags': [ClientFlag.SSL],
        'ssl_ca': 'server-ca.pem',
        'ssl_cert': 'client-cert.pem',
        'ssl_key': 'client-key.pem'
    }

    # now we establish our connection
    cnxn = mysql.connector.connect(**config)


    cursor = cnxn.cursor()  # initialize connection cursor
    cursor.execute('CREATE DATABASE IF NOT EXISTS testdb')  # create a new 'testdb' database
    cnxn.close()  # close connection because we will be reconnecting to testdb

    config['database'] = 'testdb'  # add new database to config dict
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()

    cursor.execute("DROP TABLE {tab}".format(tab=monster_name))

    cursor.execute("CREATE TABLE IF NOT EXISTS {tab} (name VARCHAR(255), expiry VARCHAR(255), blank_first VARCHAR(255), blank_second VARCHAR(255), alive VARCHAR(255), expired VARCHAR(255), last_updated VARCHAR(255), earliest_expiry VARCHAR(255));".format(tab=monster_name))

    cnxn.commit()  # this commits changes to the database

    sql = "INSERT INTO {tab} (name, expiry, blank_first, blank_second, alive, expired, last_updated, earliest_expiry) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)".format(tab=monster_name)


    cursor.executemany(sql, data)

    cnxn.commit()

    cursor.execute("SELECT * FROM elite_bloodfang;")
    res = cursor.fetchall()
    for row in res:
        print(row)
    cnxn.close()