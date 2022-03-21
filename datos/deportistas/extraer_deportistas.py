'''
Programa que extrae los datos de https://www.imdb.com/chart/top/
y genera un json con los datos de las películas
Trabajo: 
* Inspeccionar la estructura de la web
* Extraer los datos de las películas con xpath
'''

import requests
from lxml import html
from urllib.parse import urljoin
import json
import requests


headers = {"Accept-Language": "es-es,es;q=0.5"}






def datos_deportistas(deportista):
    ''''
    Función que dado un elemento tr de imdb con 
    los datos de una película devuelve un diccionario
    con los datos de ...
    '''
    # datos a devolver
    datos = {}



    elementos  = deportista.xpath("//table[contains(caption, 'Ganadores y')]")[0] 
    nombre = elementos[0]
    pais= elementos[2]   
    deporte= elementos[3]






    nombree = nombre.xpath(".//tbody/tr")[0]
    datos['nombre'] = nombree
    
    paiss= pais.xpath(".//td")[2].text_content() 
    datos['país'] = paiss
    
    deportee= deporte.xpath(".//td")[3].text_content()
    datos['deporte'] = deportee
    
    return datos

if __name__ == '__main__':

    url = 'https://es.wikipedia.org/wiki/Anexo:Premio_Laureus_al_Mejor_Deportista_Masculino_Internacional_del_A%C3%B1o'
    datos = []
    for x in range(1, 4):
    
        response = requests.get(url.format(x), headers=headers)
        pagina = html.fromstring(response.text)

        deportistas = pagina.xpath("//table[contains(caption, 'Ganadores y')]")

        

        datos.extend([datos_deportistas(d) for d in deportistas])
    json.dump(datos, open('datos_deportistas.json', 'w'))




