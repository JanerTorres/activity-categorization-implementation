import json
from Author import Author
from Institution import Institution


with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
    articles = json.loads(dataUdeA.read())

"""en un principio lo que hace es extraer la información del JSON, crear y actulizar los atributos de los objetos
con base a esta información"""

authors = []
institutions = []
fields_of_study = []
authors_existence = []
institutions_existence = []

"""For que recorre articles, siendo articles una lista de los articulos que están en el JSON"""

for i in articles:
    """Debido a que en el JSON los autores vienen dados por un solo string y lo único que diferencia
     un autor de otro es un ; utilizamos split() que nos genera una lista con los autores ya separados,
      lo mismo hacemos para instituciones y temas"""
    _article = i.get('Title')
    _authors = i.get('Author').get('s').split("; ")
    _institutions = i.get('Funding').split("; ")
    _fields = i.get('Fields of Study').split("; ")

    """Aquí por cada Artículo recorremos las listas de instituciones y autores para crear los objetos o 
    en caso de que ya existan actulizar sus atributos"""

    for insti in _institutions:
        if insti not in institutions_existence:
            institutions_existence += [insti]
            institutions += [Institution(insti, _authors, _fields, [_article])]
        else:
            pos = institutions_existence.index(insti)

            for author in _authors:
                if author not in institutions[pos].author:
                    institutions[pos].author += [author]

            for field in _fields:
                if field not in institutions[pos].fields:
                    institutions[pos].fields += [field]

            if _article not in institutions[pos].articles:
                institutions[pos].articles += [_article]

    for c in _authors:
        if c not in authors_existence:
            authors_existence += [c]
            authors += [Author(c, _institutions, _fields, _article)]
        else:
            pos = authors_existence.index(c)

            authors[pos].articles += [_article]

            for field in _fields:
                if field not in authors[pos].fields:
                    authors[pos].fields += [field]

            for institution in _institutions:
                if institution not in authors[pos].institutions:
                    authors[pos].institutions += [institution]

            if _article not in authors[pos].articles:
                authors[pos].articles += _article

    for field in _fields:
        if (not field == "") and (field not in fields_of_study):
            fields_of_study += [field]


def institution_search():
    search = ""
    found_institutions = []
    while search == "":
        search = input('Introduzca Institución a Buscar: ')
    search = search.lower()
    for institution in institutions:
        if institution.institution.lower().__contains__(search):
            found_institutions += [institution]

    for pos in range(len(found_institutions)):
        print(pos, "- ", found_institutions[pos].institution)

    option = ""
    while option == "":
        print()
        option = input("Ingrese el número de una Institución para ver su información: ")
        try:
            option = int(option)
            if int(option) < 0 or int(option) >= len(found_institutions):
                option = ""
                print("Opción Invalida")
        except:
            print("Opción Invalida")
            option = ""

    print()
    print("Nombre: ", found_institutions[option].institution)
    print("Autores: ", found_institutions[option].author)
    print("Temas: ", found_institutions[option].fields)
    print("Articulos: ", found_institutions[option].articles)


def field_search():
    search = ""
    found_fields = []
    while search == "":
        search = input('Introduzca Tema a buscar: ')
    search = search.lower()
    for field in fields_of_study:
        if field.lower().__contains__(search):
            found_fields += [field]

    for pos in range(len(found_fields)):
        print(pos, "- ", found_fields[pos])

    option = ""
    while option == "":
        print()
        option = input("Ingrese el número de un Tema para buscar Instituciones relevantes: ")
        try:
            option = int(option)
            if int(option) < 0 or int(option) >= len(found_fields):
                option = ""
                print("Opción Invalida")
        except:
            print("Opción Invalida")
            option = ""

    option = found_fields[option]
    found_institutions = []
    for institution in institutions:
        if option in institution.fields:
            found_institutions += [institution]

    print()
    print("Instituciones con relación al Tema: ")
    for institution in found_institutions:
        print(institution.institution)

field_search()
