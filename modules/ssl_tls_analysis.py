import ssl, socket

def get_cert_info(domain):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
        s.settimeout(3)
        try:
            s.connect((domain, 443))
            cert = s.getpeercert()
            return cert
        except Exception as e:
            return {"error": str(e)}

