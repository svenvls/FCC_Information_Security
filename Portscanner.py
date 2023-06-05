#!/usr/bin/python3

import socket

def portScanner(host, port):
    """
    Controleert of een specifieke poort op een gegeven host open is of gesloten.

    Args:
        host (str): Het IP-adres of de hostnaam van de doelhost.
        port (int): Het poortnummer dat moet worden gecontroleerd.

    Returns:
        None
    """
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.settimeout(5)

    try:
        result = s.connect_ex((host, port))
        if result == 0:
            print("De poort is open")
        else:
            print("De poort is gesloten")
    except socket.error as e:
        print(f"Fout bij het scannen van de poort: {e}")

    s.close()

def main():
    """
    Het hoofdprogramma dat de gebruiker vraagt om een IP-adres en poort en de poortstatus afdrukt.
    "2001:41d0:8:ccd8:137:74:187:103" Dit is www.hackthissite.org
    """
    host = input("Voer het IP-adres of de hostnaam in: ")
    port = int(input("Voer het poortnummer in: "))

    portScanner(host, port)

if __name__ == "__main__":
    main()


'''

De code is in een functie portScanner() geplaatst die verantwoordelijk is voor het scannen van de poort.
De functie portScanner() accepteert nu het host en port als parameters in plaats van deze als globale variabelen te gebruiken.
Er is een try-except blok toegevoegd om socketfouten af te vangen en een betere foutmelding weer te geven.
De socket wordt nu binnen de functie portScanner() aangemaakt en gesloten na gebruik. Dit zorgt voor een betere beheer van de resources.
Het afdrukken van de resultaten is verplaatst naar de functie portScanner() om de code beter te structureren.
Het hoofdprogramma main() vraagt de gebruiker om een IP-adres of hostnaam en een poortnummer, en roept vervolgens de portScanner() functie aan om de status van de poort af te drukken.
De code maakt gebruik van if __name__ == "__main__": om ervoor te zorgen dat de main() functie alleen wordt uitgevoerd wanneer het script rechtstreeks wordt uitgevoerd, niet wanneer het geïmporteerd wordt als een module.

'''

