import sqlite3
from sqlite3 import Error

database = r"./database.db"
##### TEST #####
sql_create_test_table = """CREATE TABLE IF NOT EXISTS test (
                                id INTEGER PRIMARY KEY,
                                data TEXT
                            );"""

sql_select_test="SELECT id, data FROM test;"   

def add_test_data(conn,id,data):
    sql_add_test_data = ''' INSERT INTO test(id,data)
              VALUES(?,?); '''
    try:
        cur= conn.cursor()
        cur.execute(sql_add_test_data,(id,data))
        conn.commit()
    except Error as e:
        print(e)
    


def test_db():
    conn = create_connection(database)
    execute(conn,sql_create_test_table)
    add_test_data(conn,1,"dette")
    add_test_data(conn,2,"er")
    add_test_data(conn,3,"en")
    add_test_data(conn,4,"test")
    test_output = execute(conn,sql_select_test)
    for (id,data) in test_output:
        print(f"{data}")
##### BASIC ####)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def execute(conn,sql_input,values=None):
    try:
        c = conn.cursor()
        c.execute(sql_input)
        print("executed input:")
        print(sql_input)
    except Error as e:
        print(e)
    return c

##### TABLES #####

tables = []

fermentable = """CREATE TABLE IF NOT EXISTS fermentable (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                dbv INTEGER NOT NULL,
                humidity INT NOT NULL
);"""
tables.append(fermentable)

hops =  """CREATE TABLE IF NOT EXISTS hops (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                aa INTEGER NOT NULL,
                humidity INT NOT NULL
);"""
tables.append(hops)

yeast =  """CREATE TABLE IF NOT EXISTS yeast (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                attenuation INTEGER NOT NULL              
);"""
tables.append(yeast)




def create_tables(conn,tables):
    conn=conn 
    for table in tables:
        execute(conn,table)


##### SETUP ######
def setup():
    conn = create_connection(database)
    if conn is not None:
        print("Success database created!")
        conn.close

if __name__ == '__main__':
    print("initializing database")
    setup()
    print("testing database")
    test_db()