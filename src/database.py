import sqlite3
# SIEMPRE se debe trabjar usando los metodos de esta clase, se debe evitar a toda cosa usar funciones sqlite directas
# para evitar problemas
class ClaseDB:
    def __init__(self,nombre_db):
        self.conexion = sqlite3.connect(nombre_db)
        self.cursor = self.conexion.cursor()

    def crear_modelo_base(self):
        # activamos las claves foraneas
        self.conexion.execute("PRAGMA foreign_keys = ON")
        # Tablas maestras
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuario(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, password TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS grado_instruccion(id_grado INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cargo(id_cargo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tipo_personal(id_tipo_personal INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS estado_laboral(id_estado_laboral INTEGER PRIMARY KEY AUTOINCREMENT, descripcion TEXT)")

        # Tabla principal
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS personal (
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                cedula INTEGER,
                nombres TEXT,
                apellidos TEXT,
                direccion TEXT,
                correo TEXT,
                telefono TEXT,
                carnet_patria TEXT,
                comuna TEXT,
                titulo_obtenido TEXT,
                id_grado INTEGER,
                id_cargo INTEGER,
                id_tipo_personal INTEGER,
                id_estado_laboral INTEGER,

                FOREIGN KEY (id_grado) REFERENCES grado_instruccion (id_grado),
                FOREIGN KEY (id_cargo) REFERENCES cargo (id_cargo),
                FOREIGN KEY (id_tipo_personal) REFERENCES tipo_personal (id_tipo_personal),
                FOREIGN KEY (id_estado_laboral) REFERENCES estado_laboral (id_estado_laboral)
            )
        """)

    def print_tabla(self,tabla):  ### abandonado #### NO USAR
        self.cursor.execute(f"SELECT * FROM {tabla}")
        print(self.cursor.fetchall())
        return self.cursor.fetchall()

    def consultar(self,sql):
        self.cursor.execute(sql)
        self.conexion.commit()
        return self.cursor.fetchall()

    def cerar(self):
        self.conexion.close()
