import socket

def banner(ip, port):
    """
    Maakt verbinding met het opgegeven IP-adres en poort en ontvangt een banner van de server.

    Args:
        ip (str): Het IP-adres waarmee verbinding moet worden gemaakt.
        port (str): De poort waarmee verbinding moet worden gemaakt.

    Returns:
        None
    """
    with socket.socket() as s:
        s.settimeout(10)
        try:
            s.connect((ip, int(port)))
            print(s.recv(1024).decode().strip())
        except socket.error as e:
            print(f"Fout: {e}")

def main():
    """
    Het hoofdprogramma dat de gebruiker vraagt om een IP-adres en poort en de banner van de server afdrukt.
    """
    ip = input("Voer het IP-adres in: ")
    port = input("Voer de poort in: ")
    banner(ip, port)

if __name__ == "__main__":
    main()


'''

De code maakt gebruik van de socket module om een verbinding te maken met een server en een banner van de server te ontvangen.
De functie banner() maakt een socket object aan en maakt verbinding met het opgegeven IP-adres en de poort.
Er wordt een timeout van 10 seconden ingesteld op de socket met settimeout(10) om te voorkomen dat het programma onnodig lang wacht op een respons van de server.
Als er een succesvolle verbinding tot stand is gebracht, wordt een bericht van maximaal 1024 bytes ontvangen en gedecodeerd van bytes naar een string met decode(). De strip() methode wordt gebruikt om eventuele witruimte aan het begin en einde van de string te verwijderen.
Als er een socket fout optreedt tijdens het maken van de verbinding, wordt een foutmelding afgedrukt met de relevante foutinformatie.
Het hoofdprogramma main() vraagt de gebruiker om een IP-adres en poort en roept vervolgens de banner() functie aan om de banner van de server af te drukken.
De code maakt gebruik van if __name__ == "__main__": om ervoor te zorgen dat de main() functie alleen wordt uitgevoerd wanneer het script rechtstreeks wordt uitgevoerd, niet wanneer het geïmporteerd wordt als een module.

'''