from database import *
import tkinter as tk
from tkinter import ttk


db = ClaseDB(":memory:")
db.crear_modelo_base()

# Grados de Instrucción
grados = [("Bachiller",), ("Técnico Medio",), ("Licenciado",), ("Ingeniero",), ("Magister",)]
db.cursor.executemany("INSERT INTO grado_instruccion (nombre) VALUES (?)", grados)

# Cargos
cargos = [("Analista",), ("Supervisor",), ("Gerente",), ("Asistente",), ("Obrero",)]
db.cursor.executemany("INSERT INTO cargo (nombre) VALUES (?)", cargos)

# Tipos de Personal
tipos = [("Fijo",), ("Contratado",), ("Comisión de Servicio",)]
db.cursor.executemany("INSERT INTO tipo_personal (nombre) VALUES (?)", tipos)

# Estados Laborales
estados = [("Activo",), ("Reposo",), ("Vacaciones",), ("Jubilado",)]
db.cursor.executemany("INSERT INTO estado_laboral (descripcion) VALUES (?)", estados)

db.conexion.commit()

# Datos dummy para la tabla principal
# Nota: id_grado, id_cargo, id_tipo, id_estado son los números que insertamos arriba
datos_personal = [
    (20032323, "Yusepe", "Aranguren", "Calle 10, Casa 5", "yusepe@mail.com", "0412-1112233", "0012345", "Comuna A", "Ing. Sistemas", 4, 3, 1, 1),
    (25987654, "Beximar", "Rodriguez", "Av. Principal 12", "bexi@mail.com", "0414-9998877", "0054321", "Comuna B", "Lic. Administracion", 3, 1, 2, 1),
    (18456123, "Carlos", "Perez", "Barrio El Centro", "carlos@mail.com", "0416-5554433", "0099887", "Comuna C", "Bachiller", 1, 5, 1, 2)
]

query_insert = """
    INSERT INTO personal (
        cedula, nombres, apellidos, direccion, correo, telefono,
        carnet_patria, comuna, titulo_obtenido,
        id_grado, id_cargo, id_tipo_personal, id_estado_laboral
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

db.cursor.executemany(query_insert, datos_personal)
db.conexion.commit()



root = tk.Tk()
root.title("Proyecto STAR")
root.geometry("2000x1000")



columnas_lista_principal = ('codigo','cedula','nombres','apellidos','direccion','correo','telefono','carnet_patria','comuna','titulo_obtenido','id_grado','id_cargo','id_tipo_personal','id_estado_laboral')
lista_principal = ttk.Treeview(root, columns=columnas_lista_principal, show="headings")
lista_principal.heading('codigo', text="codigo")
lista_principal.heading('cedula', text="cedula")
lista_principal.heading('nombres', text="nombres")
lista_principal.heading('apellidos', text="apellidos")
lista_principal.heading('direccion', text="dirrecion")
lista_principal.heading('correo', text="correo")
lista_principal.heading('telefono', text="telefono")
lista_principal.heading('carnet_patria', text="carnet P")
lista_principal.heading('comuna', text="comuna")
lista_principal.heading('titulo_obtenido', text="titulo")
lista_principal.heading('id_grado', text="grado")
lista_principal.heading('id_cargo', text="cargo")
lista_principal.heading('id_tipo_personal', text="Tipo Personal")
lista_principal.heading('id_estado_laboral', text="Estado laboral")

lista_principal.pack(fill="both",expand=True)



for registro in db.consultar("SELECT * from personal"):
    lista_principal.insert("", "end", values=registro)
root.mainloop()
