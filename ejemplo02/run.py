import requests
import json
from config import url_base

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    data = json.load(f)

base_datos = "personas002"

# AGREGAR: Crear la base de datos si no existe
url_crear_db = f"{url_base}/{base_datos}"
response_crear = requests.put(url_crear_db)
if response_crear.status_code == 201:
    print(f"Base de datos '{base_datos}' creada exitosamente")
elif response_crear.status_code == 412:
    print(f"Base de datos '{base_datos}' ya existe")
else:
    print(f"Error al crear base de datos: {response_crear.status_code}")
    print(response_crear.json())

# Configurar el acceso a la base de datos
url = f"{url_base}/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
response = requests.post(url, headers=headers, json=data)

# Mostrar respuesta
print(response.status_code)
print(response.json())