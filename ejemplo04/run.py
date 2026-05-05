import requests
import json
from config import URL_BASE, AUTH, LETRAS_FILTRO

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    data = json.load(f)

# Filtrar datos
lista_datos = [d for d in data['docs'] if d['nombre'][0] in LETRAS_FILTRO]

base_datos = "personas004"
url = f"{URL_BASE}/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos uno por uno
for doc in lista_datos:
    response = requests.post(url, json=doc, auth=AUTH)
    print(f"Insertando {doc['nombre']} | {response.status_code}")
    
''' - Ejemplo 3: Eficiente para insertar muchos datos a la vez (inserción batch/masiva)
    - Ejemplo 4: Inserción secuencial, documento por documento (menos eficiente pero más controlado)

        Ambos están parametrizados con config.py, pero la diferencia clave es el método de inserción.'''