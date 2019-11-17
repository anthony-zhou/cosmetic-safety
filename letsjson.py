import json
from imaging import text_words
from toxic import gettoxicity

with open('chemical-data/chemical_list.json') as json_file:
    chemicallist = json.load(json_file)
with open("chemical-data/class_uses_and_risks.json") as json_file:
    chemicaluses = json.load(json_file)

def letsjson(lst):
    dct = {}
    for foundchemical in lst:
        for chemical in chemicallist:
            if chemical['Name'].lower() == foundchemical.lower():
                finchem = foundchemical.lower()
                good = False
                for clas in chemicaluses:
                    if clas['Class'].lower() == chemical['Class'].lower():
                        attribute = clas['Risks']
                        good = True
                if not good:
                    attribute = "Associated with " + ", ".join(list(gettoxicity(foundchemical))) + "."
                dct[finchem] = attribute
    return dct

def getjson(img):
    lst = text_words(img)
    dct = letsjson(lst)
    return dct

if __name__=="__main__":
    print(getjson("/Users/nathaniel/PycharmProjects/cosmetic-safety/6887285_nocolor_4.jpg"))