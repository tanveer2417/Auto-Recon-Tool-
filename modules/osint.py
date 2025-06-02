import socket
import re
import whois

def gather_osint(domain):
    try:
        data = whois.whois(domain)
        emails = set(re.findall(r'[\w\.-]+@[\w\.-]+', str(data)))
        return {
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "emails": list(emails)
        }
    except Exception as e:
        return {"error": str(e)}

