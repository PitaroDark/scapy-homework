from datetime import datetime
from sys import argv, exit
from time import sleep
from os import popen

def getDataArp():
    arp_dict = {}
    dataArp = popen('arp -n').read() 
    lines = dataArp.split('\n')

    for line in lines:
        if not line or 'incomplete' in line or line.startswith("Address"):
            continue
        parts = line.split()
        if len(parts) >= 4:
            ip = parts[0]
            mac = parts[2]
            arp_dict[ip] = mac
    return arp_dict


def main():    
    # Tiempo de espera entre cada iteración
    timeToWait = int(argv[1]) if len(argv) > 1 else 10
    print(f"Monitorizando ARP cada {timeToWait} segundos")
    previousArpTable = {}
    try:
        while True:
            currentArpTable = getDataArp()
            if previousArpTable and previousArpTable != currentArpTable:
                diff = set(previousArpTable.items()) ^ set(currentArpTable.items())
                for ip, mac in diff:
                    log_msg = f"[{datetime.now()}] Ataque detectado -> IP: {ip} con MAC: {mac}\n"
                    with open("Arp.log", "a") as log_file:
                        log_file.write(log_msg)
            previousArpTable = currentArpTable
            sleep(timeToWait)
    except KeyboardInterrupt:
        print("\nMonitorización ARP detenida por el usuario")
        exit(0)

if __name__ == "__main__":
    main()