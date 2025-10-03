import requests
import pandas as pd
from tabulate import tabulate

url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)

# * validacion de la solicitud
if response.status_code == 200:

    print("Solicitud exitosa!")

else:
    
    print ("Error")

data = response.json()

info = [(k, type(v).__name__) for k, v in data.items()]

print(tabulate(info, headers=["key","type"],tablefmt="psql"))


















#* Recorremos JSON para identificar las KEYS y su tipo
#for key, value in data.items():
   # print(f"{key}: {type(value)}")



