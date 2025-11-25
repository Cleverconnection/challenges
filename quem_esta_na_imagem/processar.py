import json
import requests

URL = "http://localhost:5006/processar"

resp = requests.post(URL, json={"imagem": "luz_azul.png"})
print(resp.json())
