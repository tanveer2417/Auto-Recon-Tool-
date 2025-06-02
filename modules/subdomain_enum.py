import requests
import concurrent.futures

def brute_force_subdomains(domain, wordlist):
    found = []
    def check(sub):
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            return f"{sub}.{domain}"
        except:
            return None
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check, word.strip()) for word in wordlist]
        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            if result:
                found.append(result)
    return found

# Example usage
if __name__ == "__main__":
    with open("config/targets.txt") as f:
        domain = f.read().strip()
    with open("wordlists/subs.txt") as f:
        wordlist = f.readlines()
    subs = brute_force_subdomains(domain, wordlist)
    print("[+] Found Subdomains:", subs)

