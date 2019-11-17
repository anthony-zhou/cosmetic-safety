import wolframalpha

def gettoxicity(item):
    if item is None:
        return ["Error"]
    item = str(item)

    appid = "JQQAVR-GA9XYEGUE2"
    client = wolframalpha.Client(appid)
    res = client.query(item)

    for pod in res.pods:
        if pod['@title'] == 'Toxicity properties':
            try:
                x = pod['subpod']['plaintext'].split(" | ")
                if x is not None:
                    return x
                else:
                    return ["harmful effects"]
            except:
                return ["harmful effects"]

