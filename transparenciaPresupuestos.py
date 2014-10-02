from bs4 import BeautifulSoup

import requests

url = "sg.nl.gob.mx/OrdenCompra_2009/BsqAnio.aspx?Anio=2012&Nombre=&EntidadId=1004&ConceptoId=308"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

print soup

