#Modulos de terceiros podem ser instalados usando o PIP
print("\nImportação e uso de modulo de terceiros")
import requests

url_ = "https://www.google.com"
response = requests.get(url_)
print(f"Solicitação http para {url_} retornou o status {response.status_code}")