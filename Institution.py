
# La clase Institution recibe el nombre de la institución como parametro único, debe ser un dato de tipo String


class Institution:

    def __init__(self, institution, author, fields, article):
        self.institution = institution
        self.author = author
        self.fields = fields
        self.articles = article
