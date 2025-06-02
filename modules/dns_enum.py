import dns.resolver

def dns_lookup(domain):
    records = {}
    try:
        records['A'] = [r.address for r in dns.resolver.resolve(domain, 'A')]
    except: records['A'] = []
    try:
        records['MX'] = [r.exchange.to_text() for r in dns.resolver.resolve(domain, 'MX')]
    except: records['MX'] = []
    try:
        records['NS'] = [r.to_text() for r in dns.resolver.resolve(domain, 'NS')]
    except: records['NS'] = []
    return records

