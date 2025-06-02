import requests

def check_live(domains):
    live = []
    for d in domains:
        try:
            r = requests.get(f"http://{d}", timeout=2)
            if r.status_code < 400:
                live.append(d)
        except:
            continue
    return live

