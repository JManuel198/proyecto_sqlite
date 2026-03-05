import sqlite3
# SIEMPRE se debe trabjar usando los metodos de esta clase, se debe evitar a toda cosa usar funciones sqlite directas
# para evitar problemas
class ClaseDB:
    def __init__(self,nombre_db):
        self.conexion = sqlite3.connect(nombre_db)
        self.cursor = self.conexion.cursor()

    def crear_modelo_base(self):
        self.cursor.execute("""CREATE TABLE personal(id INTEGER PRIMARY KEY AUTOINCREMENT, nombe text, cedula text)""")
        self.cursor.execute("""CREATE TABLE usuario(id INTEGER PRIMARY KEY AUTOINCREMENT, nombe text, password text)""")

    def print_tabla(self,tabla):
        self.cursor.execute(f"SELECT * FROM {tabla}")
        print(self.cursor.fetchall())
        return self.cursor.fetchall()

    def consultar(self,sql):
        self.cursor.execute(sql)
        self.conexion.commit()
        return self.cursor.fetchall()

    def cerar(self):
        self.conexion.close()
