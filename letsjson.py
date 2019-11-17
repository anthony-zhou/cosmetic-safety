import json
from imaging import text_words
from toxic import gettoxicity

with open('chemical-data/chemical_list.json') as json_file:
    chemicallist = json.load(json_file)
with open("chemical-data/class_uses_and_risks.json") as json_file:
    chemicaluses = json.load(json_file)

lst = text_words('/Users/nathaniel/Downloads/71WH8dvhmXL._SL1500_.jpg') + ['cyclotetrasiloxane'] + ['oxybenzone']

def letsjson(lst):
    dct = {}
    for foundchemical in lst:
        for chemical in chemicallist:
            if chemical['Name'] == foundchemical:
                finchem = foundchemical
                good = False
                for clas in chemicaluses:
                    if clas['Class'] == chemical['Class']:
                        attribute = clas['Risks']
                        good = True
                if not good:
                    attribute = "Associated with " + ", ".join(gettoxicity(foundchemical)) + "."
                dct[finchem] = attribute
    return dct

def getjson(lst):
    dct = letsjson(lst)
    return json.dumps(dct)

with open("myjson", "w") as f:
    f.write(getjson(lst))
