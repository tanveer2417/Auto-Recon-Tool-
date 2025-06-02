import requests

vuln_signatures = {
    "XSS": ["<script>alert(1)</script>", "onerror=alert(1)"],
    "SQLi": ["' OR 1=1--", "'; DROP TABLE users--"]
}

def scan_vulnerabilities(url):
    results = {}
    for vuln, payloads in vuln_signatures.items():
        for payload in payloads:
            try:
                r = requests.get(url, params={'test': payload}, timeout=3)
                if payload in r.text:
                    results[vuln] = payload
            except:
                continue
    return results or "No common vulnerabilities found."

