#!/usr/bin/python3

import nmap

def run_scan(scanner, ip_addr, scan_type):
    """
    Voert een Nmap-scan uit op het opgegeven IP-adres met het opgegeven scantype.

    Args:
        scanner (nmap.PortScanner): Het Nmap scanner object.
        ip_addr (str): Het IP-adres dat gescand moet worden.
        scan_type (str): Het gewenste scantype.

    Returns:
        None
    """
    print("NMap-versie:", scanner.nmap_version())
    scanner.scan(ip_addr, "1-1024", scan_type)
    print(scanner.scaninfo())
    print("IP-status:", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open poorten zijn:", scanner[ip_addr][scan_type].keys())

def main():
    """
    Het hoofdprogramma dat de gebruiker verwelkomt en interactie mogelijk maakt om de Nmap-scan uit te voeren.
    """
    scanner = nmap.PortScanner()

    print("Welkom, dit is een eenvoudige Nmap-automatiseringstool")
    print("<--------------------------------------------->")

    ip_addr = input("Voer het IP-adres in dat je wilt scannen: ")
    print("Het ingevoerde IP-adres is:", ip_addr)

    resp = input("""\nVoer het type scan in dat je wilt uitvoeren:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Complete Scan\n""")
    print("Je hebt gekozen voor optie:", resp)

    if resp == '1':
        run_scan(scanner, ip_addr, '-v -sS')
    elif resp == '2':
        run_scan(scanner, ip_addr, '-v -sU')
    elif resp == '3':
        run_scan(scanner, ip_addr, '-v -sS -sV -sC -A -O')
    else:
        print('Voer een geldige optie in')

if __name__ == '__main__':
    main()


'''

De code maakt gebruik van de nmap module om een Nmap-scan uit te voeren.
De functie run_scan() voert de Nmap-scan uit op het opgegeven IP-adres met het opgegeven scantype.
De functie main() is het hoofdprogramma dat de gebruiker verwelkomt en interactie mogelijk maakt om de Nmap-scan uit te voeren.
In de functie run_scan() worden verschillende resultaten van de scan afgedrukt, zoals de Nmap-versie, scaninformatie, IP-status en de geopende poorten.
Het IP-adres wordt gevraagd aan de gebruiker en opgeslagen in de variabele ip_addr.
De gebruiker wordt gevraagd om het gewenste scantype te kiezen uit een lijst van opties.
Op basis van de keuze van de gebruiker wordt de juiste run_scan() functie opgeroepen met het corresponderende scantype.
Als de gebruiker een ongeldige optie invoert, wordt er een foutmelding afgedrukt.
De code maakt gebruik van if __name__ == '__main__': om ervoor te zorgen dat de main() functie alleen wordt uitgevoerd wanneer het script rechtstreeks wordt uitgevoerd, niet wanneer het geïmporteerd wordt als een module.

'''