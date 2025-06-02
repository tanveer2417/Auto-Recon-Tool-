import requests

def detect_waf(domain):
    try:
        r = requests.get(f"http://{domain}/waf-test", timeout=3)
        if "403 Forbidden" in r.text or r.status_code == 403:
            return "Possible WAF Detected (403 Response)"
        elif "access denied" in r.text.lower():
            return "Possible WAF Detected (Access Denied Message)"
        else:
            return "No WAF detected"
    except Exception as e:
        return f"Error: {e}"

