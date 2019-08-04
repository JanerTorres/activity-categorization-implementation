


class Article:

    def __init__(self, article):
        self.article = article
        self.name = article["Title"]  # Para el nombre extrae del artículo el dato del dic con clave Title
        self.id = article["Lens ID"]  # Para el id extrae del artículo el dato del dic con clave Lens ID
        self.themes = None
        self.authors = None
        self.institution = None
