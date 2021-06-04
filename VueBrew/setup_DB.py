import sqlite3
from sqlite3 import Error
from werkzeug.security import generate_password_hash, check_password_hash

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
                aa INTEGER NOT NULL
);"""
tables.append(hops)

yeast =  """CREATE TABLE IF NOT EXISTS yeast (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                attenuation INTEGER NOT NULL              
);"""
tables.append(yeast)

users = """CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                passwordhash  TEXT NOT NULL,
                UNIQUE  (username)         
);"""
tables.append(users)

recipe ="""CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY,
                author TEXT NOT NULL,
                name TEXT NOT NULL,
                yeast TEXT NOT NULL,
                mashtemp INT NOT NULL,
                mashtime  INT NOT NULL,
                mashwater INT NOT NULL,
                strikewater INT NOT NULL,
                boiltime INT NOT NULL,
                preboilvolume INT NOT NULL,
                postboilvolume INT NOT NULL,
                UNIQUE (name),
                FOREIGN KEY (author) REFERENCES users (username)
);"""
tables.append(recipe)

recipeFermentables = """CREATE TABLE IF NOT EXISTS recipeFermentables (
                id INTEGER PRIMARY KEY,
                recipeid INT NOT NULL,
                name  TEXT NOT NULL,
                amount INT NOT NULL,
                FOREIGN KEY (recipeid) REFERENCES recipes (id)       
);"""
tables.append(recipeFermentables)

recipeHops = """CREATE TABLE IF NOT EXISTS recipehops (
                id INTEGER PRIMARY KEY,
                recipeid INT NOT NULL,
                name TEXT NOT NULL,
                amount  INT NOT NULL,
                time INT NOT NULL,
                FOREIGN KEY (recipeid) REFERENCES recipes (id)
);"""
tables.append(recipeHops)


#####USERS####
def add_user(conn, username, passwordhash):
    cur = conn.cursor()
    try:
        sql = (
            "INSERT INTO users (username, passwordhash) VALUES (?,?) "
        )
        cur.execute(sql,(username,passwordhash))
        conn.commit()
    except sqlite3.Error as err:
        return err
    else:
        print("Added user {}.".format(username))
        return "ok"
    finally:
        cur.close()

def get_user_by_name(conn,username):
    pass

def get_hash_for_login(conn, username):
    cur = conn.cursor()
    try:
        sql = (
            "SELECT passwordhash FROM users WHERE username = ? "
        )
        cur.execute(sql,(username,))
        for row in cur:
            (passwordhash,) = row
            return passwordhash
        else:
            return None
       
    except sqlite3.Error as err:
        print("Error: {}".format(err))
    else:
        print("Found Hash for {}.".format(username))
    finally:
        cur.close() 

def create_tables(tables):
    conn=create_connection(database)
    for table in tables:
        execute(conn,table)
#####DATA#####
def add_fermentable(conn, name, dbv,humidity):
    cur = conn.cursor()
    try:
        sql = (
            "INSERT INTO fermentable (name, dbv,humidity) VALUES (?,?,?) "
        )
        cur.execute(sql,(name,dbv,humidity))
        conn.commit()
    except sqlite3.Error as err:
        print("Error: {}".format(err))
    else:
        print("Added fermentable {}.".format(name))
    finally:
        cur.close()

def add_hops(conn, name, aa):
    cur = conn.cursor()
    try:
        sql = (
            "INSERT INTO hops (name, aa) VALUES (?,?) "
        )
        cur.execute(sql,(name,aa))
        conn.commit()
    except sqlite3.Error as err:
        print("Error: {}".format(err))
    else:
        print("Added hop {}.".format(name))
    finally:
        cur.close()

def add_yeast(conn, name, attenuation):
    cur = conn.cursor()
    try:
        sql = (
            "INSERT INTO yeast (name, attenuation) VALUES (?,?) "
        )
        cur.execute(sql,(name,attenuation))
        conn.commit()
    except sqlite3.Error as err:
        print("Error: {}".format(err))
    else:
        print("Added yeast {}.".format(name))
    finally:
        cur.close()

def add_recipe(conn,name,author,fermentables,hops,yeast,mashtemp,mashwater,mashtime,strikewater,boiltime,preboilvolume,postboilvolume):
    cur = conn.cursor()
    try:
        sql = (
            "INSERT INTO recipes (name,author,yeast,mashtemp,mashwater,mashtime,strikewater,boiltime,preboilvolume,postboilvolume) VALUES (?,?,?,?,?,?,?,?,?,?) "
        )
        cur.execute(sql,(name,author,yeast,mashtemp,mashwater,mashtime,strikewater,boiltime,preboilvolume,postboilvolume))
        conn.commit()
        id=get_recipe_id(conn,name)
        add_recipe_fermentables(conn,fermentables,id)
        add_recipe_hops(conn,hops,id)
    except sqlite3.Error as err:
        print(sql)
        print("Error: {}".format(err))
        return err
    else:
        return "success!"
    finally:
        cur.close()

def get_recipe_id(conn,name):
    cur = conn.cursor()
    try:
        sql = (
            "SELECT * FROM recipes WHERE name = ? "
        )
        cur.execute(sql,(name,))
        conn.commit()
        for row in cur:
            print("id")
            print(row[0])
            (id) = row[0]
            return id
    except sqlite3.Error as err:
        print(sql)
        print("Error: {}".format(err))
    else:
        return id
    finally:
        cur.close()
    return None

def add_recipe_fermentables(conn,fermentables,id):
    cur = conn.cursor()
    try:
        for fermentable in fermentables:
            name=fermentable["name"]
            print(name)
            amount=fermentable["amount"]
            print(amount)
            sql = (
                "INSERT INTO recipeFermentables (recipeid,name, amount) VALUES (?,?,?) "
            )
            cur.execute(sql,(id,name,amount))
            conn.commit()
    except sqlite3.Error as err:
        return err
    else:
        return "success!"
    finally:
        cur.close()

def add_recipe_hops(conn,hops,id):
    cur = conn.cursor()
    try:
        for hop in hops:
            name=hop["name"]
            amount=hop["amount"]
            time=hop["amount"]
            sql = (
                "INSERT INTO recipeFermentables (recipeid,name, amount,time) VALUES (?,?,?,?) "
            )
            cur.execute(sql,(id,name,amount,time))
            conn.commit()
    except sqlite3.Error as err:
        return err
    else:
        return "success!"
    finally:
        cur.close()

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
    #test_db()
    print("creating tables")
    create_tables(tables)
    conn=create_connection(database)
    print("adding user")
    add_user(conn,"testuser1",generate_password_hash("testpassword1"))
    execute_statement=execute(conn,"SELECT * FROM users")
    for (id,username,passwordhash) in execute_statement:
        print(f"{username}")
        if check_password_hash(get_hash_for_login(conn,"testuser1"),"testpassword1"):
           print("password verified")
    
        
