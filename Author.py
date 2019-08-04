

"""La clase Author recibe como parámetros:
 - author que es el nombre del autor
 - institution que es una lista de las instituciones
 - fields que es una lista de los campos de estudio
 - article que es el artículo en cual se encuentra relacionado el autor"""


class Author:

    def __init__(self, author, institutions, fields, article):
        self.author = author
        self.institutions = institutions
        self.fields = fields
        self.articles = [article]
