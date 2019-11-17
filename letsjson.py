import json
from imaging import text_words
from toxic import gettoxicity
from difflib import SequenceMatcher

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
            if lowName.capitalize() in dct:
                continue
            if found1 is not None:
                if lowName == found1 or SequenceMatcher(None, lowName, found1).ratio() > .9:
                    good = False
                    for clas in chemicaluses:
                        if clas['Class'].lower() == chemical['Class'].lower():
                            attribute = clas['Risks']
                            good = True
                    if not good:
                        attribute = "Wolfram found it is associated with " + ", ".join([j for j in (gettoxicity(lowName)) if j is not None]) + "."
                    print("Associating " + lowName + " with " + found1)
                    dct[lowName.capitalize()] = attribute
            if found2 is not None:
                if lowName == found2 or SequenceMatcher(None, lowName, found2).ratio() > .9:
                    good = False
                    for clas in chemicaluses:
                        if clas['Class'].lower() == chemical['Class'].lower():
                            attribute = clas['Risks']
                            good = True
                    if not good:
                        y = gettoxicity(lowName)
                        if y is not None:
                            x = ", ".join([j for j in y])
                            attribute = "Wolfram found it is associated with " + ", ".join([j for j in (gettoxicity(lowName)) if j is not None]) + "."
                        else:
                            attribute = "Associated with a lot of bad things."
                    print("Associating " + lowName + " with " + found1)
                    dct[lowName.capitalize()] = attribute
            if found3 is not None:
                if lowName == found3 or SequenceMatcher(None, lowName, found3).ratio() > .9:
                    good = False
                    for clas in chemicaluses:
                        if clas['Class'].lower() == chemical['Class'].lower():
                            attribute = clas['Risks']
                            good = True
                    if not good:
                        attribute = "Wolfram found it is associated with " + ", ".join([j for j in (gettoxicity(lowName)) if j is not None]) + "."
                    dct[lowName.capitalize()] = attribute
                    print("Associating " + lowName + " with " + found1)
    return dct

def getjson(img):
    lst = text_words(img)
    dct = letsjson(lst)
    return dct

if __name__=="__main__":
    print(getjson("/Users/nathaniel/Downloads/6887285_nocolor_4.jpg"))
