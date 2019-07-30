#Juan Luis Rojas Rincon
import json


with open("university_of_antioquia.json",encoding="utf-8") as dataUdeA: 
    articles=json.loads(dataUdeA.read())

def readList():
    print ("Lista de artículos")
    
    for article in articles:
        print (article)


def readField(field):
    print ("Lista de ID de artículos")

    for article in articles:
        print (article.get(field))



readList()
readField('Lens ID')


