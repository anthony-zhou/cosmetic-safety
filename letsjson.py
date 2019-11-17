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

        found1 = foundchemical.lower().replace(",", "")

        try:
            found2 = lst[lst.index(foundchemical) - 1].lower().replace(",","") + " " + found1
        except:
            found2 = ""
        try:
            found3 = found1 + " " + lst[lst.index(foundchemical) + 1].lower()
            found3 = found3.split(" ").reverse()
        except:
            found3 = ""

        for chemical in chemicallist:
            lowName = chemical['Name'].lower()
            if lowName == found1:
                good = False
                for clas in chemicaluses:
                    if clas['Class'].lower() == chemical['Class'].lower():
                        attribute = clas['Risks']
                        good = True
                if not good:
                    attribute = "Associated with " + ", ".join(list(gettoxicity(foundchemical))) + "."
                dct[found1.capitalize()] = attribute
            if lowName == found2:
                good = False
                for clas in chemicaluses:
                    if clas['Class'].lower() == chemical['Class'].lower():
                        attribute = clas['Risks']
                        good = True
                if not good:
                    attribute = "Associated with " + ", ".join(list(gettoxicity(foundchemical))) + "."
                dct[found2.capitalize()] = attribute
            if lowName == found3:
                good = False
                for clas in chemicaluses:
                    if clas['Class'].lower() == chemical['Class'].lower():
                        attribute = clas['Risks']
                        good = True
                if not good:
                    attribute = "Associated with " + ", ".join(list(gettoxicity(foundchemical))) + "."
                dct[found3.capitalize()] = attribute
    return dct

def getjson(img):
    lst = text_words(img)
    dct = letsjson(lst)
    return dct

if __name__=="__main__":
    print(getjson("/Users/nathaniel/PycharmProjects/cosmetic-safety/Screen Shot 2019-11-16 at 11.06.49 PM.png"))
