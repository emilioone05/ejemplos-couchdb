import requests
import json
from config import URL_BASE, BASE_DATOS, LETRAS_FILTRO, AUTH

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in LETRAS_FILTRO:
        lista_datos.append(d)

# Configurar el acceso a la base de datos
url = f"{URL_BASE}/{BASE_DATOS}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos con autenticación
datos_finales = {'docs': lista_datos}
response = requests.post(url, headers=headers, json=datos_finales, auth=AUTH)

print(response.status_code)
print(response.json())