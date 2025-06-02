import requests

def detect_technologies(url):
    try:
        r = requests.get(url, timeout=3)
        techs = []

        headers = r.headers
        server = headers.get('Server', '')
        x_powered_by = headers.get('X-Powered-By', '')

        if server:
            techs.append(f"Server: {server}")
        if x_powered_by:
            techs.append(f"X-Powered-By: {x_powered_by}")

        if "wp-content" in r.text:
            techs.append("WordPress Detected")
        if "/static/" in r.text:
            techs.append("Django or Flask Detected")

        return techs or ["No detectable technologies found."]
    except Exception as e:
        return [f"Error: {e}"]

