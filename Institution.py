
"""La clase Institution recibe como parámetros:
 - institution que es el nombre de la institución
 - author que es una lista de los autores relacionados
 - fields que es una lista de los campos de estudio
 - article que es el artículo relacionado con la institution"""

class Institution:

    def __init__(self, institution, author, fields, article):
        self.institution = institution
        self.author = author
        self.fields = fields
        self.articles = article
