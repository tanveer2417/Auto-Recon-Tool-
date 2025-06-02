import socket

def scan_ports(host, ports=[80, 443, 21, 22, 8080, 3306]):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports

