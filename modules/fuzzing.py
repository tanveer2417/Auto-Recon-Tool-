import requests

def fuzz_target(url, wordlist=['admin', 'login', 'backup', 'test']):
    found = []
    for path in wordlist:
        try:
            full_url = f"{url.rstrip('/')}/{path}"
            r = requests.get(full_url, timeout=2)
            if r.status_code < 400:
                found.append((full_url, r.status_code))
        except:
            continue
    return found

