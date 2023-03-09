import json

with open("E:\Code\\UPATecO\\Programacion-I\\TrabajoFinal\\Calendario\\data\\Eventos.json", 'r') as datos_json:
    dict = json.loads(datos_json)
    print(dict)