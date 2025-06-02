import requests
import re

def detect_old_versions(url):
    try:
        r = requests.get(url, timeout=3)
        old_tech = []
        patterns = {
            "jQuery": r'jquery-(1\.|2\.)\d+\.js',
            "Bootstrap": r'bootstrap\.(1|2|3)\.\d+\.min\.css'
        }
        for tech, pat in patterns.items():
            if re.search(pat, r.text):
                old_tech.append(f"{tech} (old version detected)")
        return old_tech or ["No old versions detected."]
    except Exception as e:
        return [f"Error: {e}"]

