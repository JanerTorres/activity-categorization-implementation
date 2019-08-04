import json
from Author import Author
from Institution import Institution

with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
    articles = json.loads(dataUdeA.read())

authors = []
institutions = []
authors_existence = []
institutions_existence = []

for i in articles:
    _article = i.get('Title')
    _authors = i.get('Author').get('s').split("; ")
    _institutions = i.get('Funding').split("; ")
    _fields = i.get('Fields of Study').split("; ")

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

found_authors = []

for institution in institutions:
    c = "universidad"
    c = c.lower()
    if institution.institution.lower().__contains__(c):
        found_authors += [institution.institution]
print(found_authors)

for pos in range(len(found_authors)):
    print(pos, "- ", found_authors[pos])

algo = input("Eres gay?")
print(algo)
