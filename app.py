from flask import Flask, jsonify, render_template
import netifaces
import ipaddress
import socket

try:
    from scapy.all import ARP, Ether, srp
except ImportError:
    print("Scapy non è installato. Installa scapy con: pip install scapy")
    ARP = None

app = Flask(__name__)

def get_default_gateway():
    """
    Ottiene il gateway di default e il suo indirizzo MAC
    """
    try:
        gws = netifaces.gateways()
        default_gateway_ip = gws['default'][netifaces.AF_INET][0]
        
        # Ottiene il MAC del gateway
        if ARP is not None:
            arp = ARP(pdst=default_gateway_ip)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            result = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=default_gateway_ip), timeout=2, verbose=False)[0]
            
            if result:
                gateway_mac = result[0][1].hwsrc
                try:
                    gateway_name = socket.gethostbyaddr(default_gateway_ip)[0]
                except:
                    gateway_name = "Router"
                    
                return {
                    "ip": default_gateway_ip,
                    "mac": gateway_mac,
                    "name": gateway_name
                }
        
        return {
            "ip": default_gateway_ip,
            "mac": "unknown",
            "name": "Router"
        }
    except Exception as e:
        print("Errore nel reperire il gateway:", e)
        return {
            "ip": "192.168.1.1",
            "mac": "unknown",
            "name": "Router"
        }

def get_ip_range():
    """
    Calcola il range IP locale tramite l'interfaccia predefinita.
    """
    try:
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        ip_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
        ip_addr = ip_info['addr']
        netmask = ip_info['netmask']
        network = ipaddress.IPv4Network(f"{ip_addr}/{netmask}", strict=False)
        return str(network)
    except Exception as e:
        print("Errore nel calcolare il range IP:", e)
        return "192.168.1.0/24"

def scan_devices():
    """
    Esegue una scansione ARP sull'intera rete ed esclude il gateway.
    """
    ip_range = get_ip_range()
    gateway_info = get_default_gateway()
    gateway_ip = gateway_info["ip"]
    
    if ARP is None:
        return []
        
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    
    try:
        result = srp(packet, timeout=3, verbose=False)[0]
    except Exception as e:
        print("Errore durante la scansione ARP:", e)
        return []
        
    devices = []
    for sent, received in result:
        ip = received.psrc
        # Salta il gateway
        if ip == gateway_ip:
            continue
            
        mac = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except Exception:
            hostname = ip
        devices.append({"ip": ip, "mac": mac, "name": hostname})
    
    return devices

@app.route('/data')
def data():
    """
    Restituisce in JSON i dati del gateway e la lista dei dispositivi connessi.
    """
    gateway_info = get_default_gateway()
    devices = scan_devices()
    return jsonify({
        "gateway": gateway_info,
        "devices": devices
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
