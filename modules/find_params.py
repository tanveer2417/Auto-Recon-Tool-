import requests

def find_parameters(url, params=['id', 'q', 'search', 'page']):
    reflected = []
    for p in params:
        test = {p: "test123"}
        try:
            r = requests.get(url, params=test, timeout=3)
            if "test123" in r.text:
                reflected.append(p)
        except:
            continue
    return reflected

