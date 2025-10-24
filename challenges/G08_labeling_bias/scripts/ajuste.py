import json
import requests

BASE_URL = "http://localhost:5008"

registros = requests.get(f"{BASE_URL}/dados").json()["registros"]
for registro in registros:
    if registro["tom_de_pele"] == "escuro" and registro["atributo"] == "neutro":
        registro["atributo"] = "respeitado"

resp = requests.post(f"{BASE_URL}/corrigir", json={"registros": registros})
print(resp.json())
