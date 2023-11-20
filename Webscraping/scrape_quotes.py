#Luis Cipriano Rodriguez Gonzalez
#1753573
import requests
import csv
from bs4 import BeautifulSoup
#Dirección de la página web
url = "http://quotes.toscrape.com/"
#Ejecutar GET-Request 
response = requests.get(url)
#Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup (response.text, 'html.parser')
#Extraer todas las citas y autores del archivo HTML
quotes_html=html.find_all('span', class_="text")
authors_html = html.find_all('small',class_="author")
#Crear una lista de las citas
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)
# Crear una lsita de los autores
authors = list()
for author in authors_html:
    authors.append(author.text)
# Para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
#Guardar las citas y los autores en un archivo CSV en el directorio actual
with open('./citas_1753573.csv', 'w') as cvs_file: ##CAMBIAR NOMBRE AL ARCHIVO CSV##
    csv_write = csv.writer(cvs_file, dialect='excel')
    csv_write.writerows(zip(quotes, authors))