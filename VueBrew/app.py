from setup_DB import  *
from flask import Flask
from flask import g

app = Flask(__name__)

#Application config
DATABASE = "database.db"
app.secret_key = "they_serve_pints_here"

def get_db():
    if not hasattr(g,"_database"):
        g._database = sqlite3.connect(DATABASE)
    return g._database

@app.teardown_appcontext
def teardown_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)