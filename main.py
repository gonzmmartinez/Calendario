from datetime import date, datetime
import json

class Evento:
    id = 0

    def __init__(self):
        self.recordatorio = 30
        Evento.id += 1


    def DefinirNombre(self, nombre: str):
        self.nombre = nombre

    def DefinirDescripcion(self, descripcion: str):
        self.descripcion = descripcion

    def DefinirFechaHora(self, fecha:tuple, hora:tuple):
        self.fecha = fecha
        self.hora = hora

    def DefinirRecordatorio(self, tiempo):
        self.recordatorio = tiempo

    def GuardarEvento(self):
        datos = {'Nombre': self.nombre,
                 'Descripcion': self.descripcion,
                 'Fecha': self.fecha,
                 'Hora': self.hora,
                 'Recordatorio': self.recordatorio}
        with open(f"E:\Code\\UPATecO\\Programacion-I\\TrabajoFinal\\Calendario\\data\\{Evento.id}.json", 'w') as datos_json:
            json.dump(datos, datos_json)

x = Evento()
x.DefinirNombre('Nacimiento')
x.DefinirDescripcion('Cuándo nací yo')
x.DefinirFechaHora((28,8,1998), (10,51))
x.DefinirRecordatorio(15)
x.GuardarEvento()

y = Evento()
y.DefinirNombre('Nacimiento de papá')
y.DefinirDescripcion('Cuándo nació mi papá')
y.DefinirFechaHora((24,12,1966), (21,58))
y.DefinirRecordatorio(25)
y.GuardarEvento()