#Juan Luis Rojas Rincon
import json
from Institution import Institution

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

list_institutions = []

def create_institutions():
        for var in articles:
                insts_name = var['Funding']
                aux_list = insts_name.split("; ")

                for inst_name in aux_list:
                        new_inst = Institution(inst_name)
                        list_institutions.append(new_inst)
                        print((inst_name).encode('utf-8'))
                        new_inst.update_themes()



udea = Institution("Universidad de Antioquia")
print(udea.name)

create_institutions()


#readList()
#readField('Lens ID')
