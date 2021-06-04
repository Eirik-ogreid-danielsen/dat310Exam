from setup_DB import add_recipe
from setup_DB import add_user
from werkzeug.security import check_password_hash, generate_password_hash
from setup_DB import get_hash_for_login
from setup_DB import  *
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask import g
import json

app = Flask(__name__)
CORS(app)

#Application config
DATABASE = "database.db"
app.secret_key = "they_serve_pints_here"

#registration and login
def valid_login(username, password):
    conn = get_db()
    hash = get_hash_for_login(conn, username)
    if hash == None:
        return False
    return check_password_hash(hash,password)

def get_user_id(username):
    conn = get_db()
    cur = conn.cursor()
    sql =("SELECT id FROM users WHERE username = ?")
    cur.execute(sql,(username,))
    for row in cur:
        id =  row
        return id


#######boilerplate######
def get_db():
    if not hasattr(g,"_database"):
        g._database = sqlite3.connect(DATABASE)
    return g._database

@app.teardown_appcontext
def teardown_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type,Content-Length, Authorization"
    return response

#####Functions for API######
def get_fermentables():
    conn = get_db()
    cur= conn.cursor()
    sql = "SELECT * From fermentable"
    cur.execute(sql)
    fermentables = []
    for row in cur:
        fermentable={"id":row[0],"name":row[1],"dbv":row[2],"humidity":row[3]}
        fermentables.append(fermentable)
    return fermentables

def get_hops():
    conn = get_db()
    cur= conn.cursor()
    sql = "SELECT * From hops"
    cur.execute(sql)
    hops = []
    for row in cur:
        hop={"id":row[0],"name":row[1],"aa":row[2]}
        hops.append(hop)
    return hops

def get_yeasts():
    conn = get_db()
    cur= conn.cursor()
    sql = "SELECT * From yeast"
    cur.execute(sql)
    yeasts = []
    for row in cur:
        yeast={"id":row[0],"name":row[1],"attenuation":row[2]}
        yeasts.append(yeast)
    return yeasts

def get_recipe_fermentables(id):
    
    conn = get_db()
    cur= conn.cursor()
    sql = "SELECT * From recipeFermentables WHERE recipeid = ?"
    cur.execute(sql,(id,))
    fermentables = []
    for row in cur:
        fermentable={"name":row[2],"amount":row[3]}
        print(fermentable)
        fermentables.append(fermentable)
    print(fermentables)
    return fermentables

def get_recipe_hops(id):
    
    conn = get_db()
    cur= conn.cursor()
    sql = "SELECT * From recipehops WHERE recipeid = ?"
    cur.execute(sql,(id,))
    hops = []
    for row in cur:
        hop={"name":row[2],"amount":row[3],"time":row[4]}
        print(hop)
        hops.append(hop)
    print(hops)
    return hops

def get_recipes():
    conn = get_db()
    cur=conn.cursor()
    sql = "SELECT * FROM recipes"
    cur.execute(sql)
    recipes = []
    for row in cur:
        print(row[0])
        fermentables=get_recipe_fermentables(row[0])
        print(fermentables)
        hops=get_recipe_hops(row[0])
        print(hops)
        recipe ={
            "id":row[0],
            "author":row[1],
            "name":row[2],
            "fermentables":fermentables,
            "hops":hops,
            "yeast":row[3],
            "mashtemp":row[4],
            "mashtime":row[5],
            "mashwater":row[6],
            "strikewater":row[7],
            "boiltime":row[8],
            "preboilvolume":row[9],
            "postboilvolume":row[10],
        }
        recipes.append(recipe)
    return recipes

#####API#####
@app.route('/')
def hello():
    return app.send_static_file("index.html")

@app.route('/fermentables', methods=["GET"])
def send_fermentables():
    fermentables = get_fermentables()
    return json.dumps(fermentables)

@app.route('/hops', methods=["GET"])
def send_hops():
    hops=get_hops()
    return json.dumps(hops)

@app.route('/yeasts', methods=["GET"])
def send_yeasts():
    yeasts = get_yeasts()
    return json.dumps(yeasts)

@app.route("/login", methods=["GET", "POST"])
@cross_origin()
def login_user():
    if request.method == "POST":
        username =request.json["username"]
        password = request.json["password"]
        if valid_login(username,password):
            userID = get_user_id(username)
            user = {
                "id":userID,
                "username":username
            }
            return json.dumps(user)
        else:
            return "DENIED!!!!!!!"

@app.route("/register", methods=["GET","POST"])
@cross_origin()
def create_user():
    if request.method  == "POST":
        username =request.json["username"]
        password = request.json["password"]
    conn=get_db()
    response = add_user(conn,username,generate_password_hash(password) )
    return json.dumps(response)

@app.route("/saveRecipe",methods=["GET","POST"])
@cross_origin()
def save_recipe():
    
    if request.method  == "POST":
        
        conn=get_db()
        recipename=request.json["name"]
        author=request.json["user"]
        fermentables=request.json["fermentables"]
        hops=request.json["hops"]
        yeast=request.json["yeast"]
        mashtemp=request.json["mashtemp"]
        mashtime=request.json["mashtime"]
        mashwater=request.json["mashwater"]
        strikewater=request.json["strikewater"]
        boiltime=request.json["boiltime"]
        preboilvolume=request.json["preboilvolume"]
        postboilvolume=request.json["postboilvolume"]
        add_recipe(conn,recipename,author,fermentables,hops,yeast,mashtemp,mashwater,mashtime,strikewater,boiltime,preboilvolume,postboilvolume)
    return "ok"
        


if __name__ == "__main__":
    app.run(debug=True)
    
    