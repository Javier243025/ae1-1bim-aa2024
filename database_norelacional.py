"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

# se obtiene la colección general (base de datos) 
db= client.basenorelacional
coleccion1 = db.LocalComida
coleccion2 = db.CentroDeportivo



nuevo_local = {"nombre": "La Buena Mesa", "dirección": "Calle Falsa 123",
"tipo_cocina":"italiana"}

coleccion1.insert_one(nuevo_local)

nuevo_centro = {"nombre":"Gimnasio Fit", "direccion":"Avenida Siempre Viva 742", "tipo_deporte":"Crossfit"}

coleccion2.insert_one(nuevo_centro)

print("ültimo local ingresado")
local = coleccion1.find_one()
print(local)

print("ültimo centro ingresado")
centro = coleccion2.find_one()
print(centro)
