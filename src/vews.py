from database import *

db = ClaseDB(":memory:")
db.consultar("CREATE TABLE personas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, cedula TEXT)")

db.consultar("INSERT INTO personas (nombre, cedula) VALUES ('yusepe', 'V-20032323')")
db.consultar("INSERT INTO personas (nombre, cedula) VALUES ('beximar', 'V-20032323')")

print(db.consultar("SELECT nombre FROM personas"))
