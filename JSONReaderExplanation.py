# Nato Gourmet
import json

# Esto guarda los datos del JSON en una lista, NO TOCAR
with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
    articles = json.loads(dataUdeA.read())

# Esto imprime los articulos, no es gran cosa, se puede quitar
def readList():
    print("Lista de artículos")

    for article in articles:
        print(article)


""" 
Esto imprime un campo del diccionario, I M P O R T A N T E    in english: I M P O R T A N T     es casi lo mismo pero quiero redundar en que es I M P O R T A N T E      (ven?, ahí lo hice otra vez)
A partir de ese _for_ podemos hacer toda nuestra lógica, la cual se basará en:
Por ejemmplo, si quieremos tomar el titulo del articulo, como el ejemplo que dejé (antes decía 'field', pero en el nuevo JSON, ya no existe ese campo en la primer lista) llamaremos la función enviando 'title'. (vease articulo.py)
Aclarar que ésta función solo funcionará con los campos que estén en la primera sección del _diccionario_, si ocupamos campos de un subddiccionario, debemos crear nuestra propia función. (vease la siguiente función)
"""
def readField(field):
    print("Lista de ID de artículos")

    for article in articles:
        print(article.get(field))


"""
Ahora si, con esto ya deberían entender todo a la perfección, éste metodo nos permite tomar una de las Instituciones a las que está afiliado un autor, ¿cómo hacemos esto? (vease articulo.py para entender lo siguiente)
En el primer nivel de uno de los diccionarios (articulo) tenemos 'authors' el cual es una lista, lo tomamos con .get('authors'), luego yo ingresaré al primer autor con [0], ustedes hacen un _for_ para eso.
Luego tomo el campo 'affiliations' el cual es otra lista, lo tomamos con .get('affiliations'), luego yo ingresaré a la primer afiliación con [0], ustedes hacen un _for_ para eso (nuevamente).
Finalmente hacemos un .get('name') para tomar el nombre de la Institución a la que está afiliada el autor.
"""
def readSubfield():
    print("Lista de Instituciones Afiliadas a Autores de Artículos")

    for article in articles:
        print(article.get('authors')[0].get('affiliations')[0].get('name'))


# Invocamos a sacar info del JSON
readList()

# Liniesita estética
print()

# Invocamos a imprimir el titulo de las instituciones
readField('title')

# Liniesita estética numero dos
print()

# Invocación a esa función rara que creé
readSubfield()
