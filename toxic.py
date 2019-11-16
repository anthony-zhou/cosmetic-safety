import wolframalpha

def gettoxicity(item):

    item = str(item)

    app_id = 'JQQAVR-5RY4HPRUV3'
    client = wolframalpha.Client(app_id)
    res = client.query(item)

    for pod in res.pods:
        if pod['@title'] == 'Toxicity properties':
            return pod['subpod']['plaintext'].split(" | ")
