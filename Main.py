import json
from AuthorF import Author

with open("university_of_antioquia.json", encoding="utf-8") as dataUdeA:
    articles = json.loads(dataUdeA.read())



