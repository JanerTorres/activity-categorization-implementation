import json

with open("university_of_antioquia.json",encoding="utf-8") as dataUdeA:
    articles=json.loads(dataUdeA.read())

class Institution:

    def __init__(self, name):
        self.name = name
        self.themes = []
        self.authors = []
        print("Institution created correctly")

    def update_themes(self):
        for var in articles:
            inst = var['Funding']
            inst_list = inst.split(";")
            for x in inst_list:
                if(len(x) > 1):
                    if(x is self.name):
                        aux_themes = var['Fields of Study']
                        themes_list = aux_themes.split(";")
                        for theme in themes_list:
                            self.themes.append(theme)
                            print(theme)
            
            #if(i_found != -1 or len(var['Funding']) > 0 ):
                #aux_themes = var['Fields of Study']
                #themes_list = aux_themes.split(";")
                #for theme in themes_list:
                    #self.themes.append(theme)
                    #print(theme)

                    #len(self.name) > 0 and x is self.name

