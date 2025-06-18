#Gestor Persistencia Json
#codigo editable para realizar pruebas de carga y persistencia de datos en diferentes entornos

import json
from datetime import datetime

class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.completada = False

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_limite": self.fecha_limite,
            "completada": self.completada
        }

    @staticmethod
    def from_dict(data):
        t = Tarea(data['titulo'], data['descripcion'], data['fecha_limite'])
        t.completada = data['completada']
        return t

class GestorTareas:
    def __init__(self, archivo='tareas.json'):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        try:
            with open(self.archivo, 'r') as f:
                data = json.load(f)
                return [Tarea.from_dict(t) for t in data]
        except FileNotFoundError:
            return []

    def guardar_tareas(self):
        with open(self.archivo, 'w') as f:
            json.dump([t.to_dict() for t in self.tareas], f, indent=4)

    def agregar_tarea(self, titulo, descripcion, fecha_limite):
        self.tareas.append(Tarea(titulo, descripcion, fecha_limite))
        self.guardar_tareas()

    def listar_tareas(self):
        for idx, tarea in enumerate(self.tareas):
            estado = "✅" if tarea.completada else "❌"
            print(f"{idx+1}. {tarea.titulo} - {estado}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            self.guardar_tareas()

# Este codigo es reutilizable para diferentes tipos de pruebas
if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n1. Agregar tarea\n2. Listar tareas\n3. Completar tarea\n4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            gestor.agregar_tarea(titulo, descripcion, fecha)
        elif opcion == '2':
            gestor.listar_tareas()
        elif opcion == '3':
            idx = int(input("Número de tarea a completar: ")) - 1
            gestor.completar_tarea(idx)
        elif opcion == '4':
            break
