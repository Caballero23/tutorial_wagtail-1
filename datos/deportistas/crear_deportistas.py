

from datos.deportistas.extraer_deportistas import datos_deportistas
from deportistas.models import deportista
import json
import os


# borrar pelis
for l in deportista.objects.all():
    l.delete()

#lista de películas del json
if os.path.exists("datos/deportista/datos_deportistas.json"):
    deportistas = json.load(open("datos/deportistas/datos_deportistas.json"))
else:
    deportistas = json.load(open("datos_deportistas.json"))




for d1 in deportistas:
    d = deportistas()
    d.nombre = d1["nombre"]
    d.país = d1["país"]
    d.deporte = d1["deporte"]
    d.save()