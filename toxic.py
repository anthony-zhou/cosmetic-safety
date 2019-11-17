import wolframalpha

def gettoxicity(item):

    item = str(item)

    appid = "JQQAVR-GA9XYEGUE2"
    client = wolframalpha.Client(appid)
    res = client.query(item)

    for pod in res.pods:
        if pod['@title'] == 'Toxicity properties':
            try:
                return pod['subpod']['plaintext'].split(" | ")
            except:
                return ["harmful effects"]