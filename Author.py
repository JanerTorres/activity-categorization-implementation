

# La clase Author recibe el nombre del autor como parametro único, debe ser un dato de tipo String


class Author:

    def __init__(self, author, institutions, fields, article):
        self.author = author
        self.institutions = institutions
        self.fields = fields
        self.articles = [article]
