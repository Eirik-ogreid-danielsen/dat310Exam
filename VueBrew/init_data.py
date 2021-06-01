
from setup_DB import *

database = r"./database.db"

conn = create_connection(database)

fermentables = [{"name":"Best Pilsner","dbv":80.5,"humidity":4.9},{"name":"Best Pale Ale","dbv":80.5,"humidity":4.9},{"name":"Best Caramel Munich I","dbv":75,"humidity":4.5},{"name":"Best Caramel Hell","dbv":75,"humidity":4.5},{"name":"Best Chocolate","dbv":75,"humidity":4.5}]
yeasts = [{"name":"SafAle US-05","attenuation":82},{"name":"SafAle US-04","attenuation":78},{"name":"Belgian Tripel M31","attenuation":88},{"name":"Bavarian Wheat M20","attenuation":75},{"name":"French Saison M29","attenuation":90}]
hops = [{"name":"Hallertau Blanc","aa":10},{"name":"Hallertau Mittelfruh","aa":5},{"name":"Magnum","aa":14},{"name":"Citra","aa":14.2},{"name":"Fuggle","aa":5}]

for fermentable in fermentables: 
    add_fermentable(conn, fermentable["name"], fermentable["dbv"], fermentable["humidity"],)
for yeast in yeasts:
    add_yeast(conn, yeast["name"], yeast["attenuation"])
for hop in hops:
    add_hops(conn, hop["name"], hop["aa"])
conn.close