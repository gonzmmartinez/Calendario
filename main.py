from datetime import date, datetime
import json


class Evento:
    # Clase que simula el comportamiento de un evento simple
    id = 0

    def __init__(self):
        # Método constructor
        self.hora = None
        self.descripcion = None
        self.nombre = None
        self.fecha = None
        self.recordatorio = (30, 'minutos')
        Evento.id += 1

    def DefinirNombre(self, nombre: str):
        # Método que guarda el nombre del evento
        self.nombre = nombre

    def DefinirDescripcion(self, descripcion: str):
        # Método que guarda la descripción del evento
        self.descripcion = descripcion

    def DefinirFechaHora(self, fecha: tuple, hora: tuple):
        # Método que guarda la fecha y hora del evento
        self.fecha = fecha
        self.hora = hora

    def DefinirRecordatorio(self, tiempo: int, tipo: str):
        # Método que define el tiempo en minutos de recordatorio del evento (por defecto 30 minutos)
        self.recordatorio = (tiempo, tipo)

    def GuardarEvento(self):
        # Método que guarda los datos del evento en un archivo json
        datos = {'Nombre': self.nombre,
                 'Descripcion': self.descripcion,
                 'Fecha': self.fecha,
                 'Hora': self.hora,
                 'Recordatorio': self.recordatorio}
        with open(f"E:\Code\\UPATecO\\Programacion-I\\TrabajoFinal\\Calendario\\data\\Eventos.json", 'a') as datos_json:
            json.dump(datos, datos_json)


x = Evento()
x.DefinirNombre('Nacimiento')
x.DefinirDescripcion('Cuándo nací yo')
x.DefinirFechaHora((28, 8, 1998), (10, 51))
x.DefinirRecordatorio(2, 'horas')
x.GuardarEvento()

y = Evento()
y.DefinirNombre('Nacimiento de papá')
y.DefinirDescripcion('Cuándo nació mi papá')
y.DefinirFechaHora((24, 12, 1963), (21, 58))
y.DefinirRecordatorio(25, 'minutos')
y.GuardarEvento()
