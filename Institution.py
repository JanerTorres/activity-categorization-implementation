


# La clase Institution recibe el nombre de la institución como parametro único, debe ser un dato de tipo String


class Institution:

    def __init__(self, institution):
        self.institution = institution
        self.author = []
        self.themes = []
        self.articles = None