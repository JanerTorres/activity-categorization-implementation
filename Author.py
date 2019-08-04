

# La clase Author recibe el nombre del autor como parametro único, debe ser un dato de tipo String


class Author:

    def __init__(self, author):
        self.author = author
        self.institution = []
        self.themes = []
        self.articles = None