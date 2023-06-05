import socket

# Een socket object maken voor de server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Het verkrijgen van de hostnaam van de huidige machine
host = socket.gethostname()
# De poort waarnaar de server luistert
port = 444

# Binden van het socket object aan het hostadres en de poort
serverSocket.bind((host, port))

# Luisteren naar inkomende verbindingen met een maximum van 3 wachtrijen
serverSocket.listen(3)

# Oneindige lus om verbindingen te accepteren
while True:
    # Accepteren van een inkomende verbinding van een client
    # clientSocket is het socket object voor de geaccepteerde verbinding
    # address is het adres van de client
    clientSocket, address = serverSocket.accept()
    
    # Het afdrukken van de geaccepteerde verbinding
    print("Verbinding ontvangen van", address)

    # Het bericht dat naar de client wordt gestuurd
    message = "Bedankt voor het verbinden met de server\r\n"
    
    # Het versturen van het bericht naar de client
    clientSocket.send(message.encode('ascii'))

    # Sluiten van de verbinding met de client
    clientSocket.close()

''' 
Verbeteringen:

De code maakt gebruik van de socket module om een server te maken die luistert naar inkomende verbindingen.
Er wordt een socket object gemaakt voor de server met het adresfamilie AF_INET en het sockettype SOCK_STREAM.
De hostnaam wordt verkregen met behulp van socket.gethostname() en opgeslagen in de variabele host.
De poort wordt ingesteld op 444 en opgeslagen in de variabele port.
Het socket object wordt gebonden aan het hostadres en de poort met behulp van de bind()-methode.
De server luistert naar inkomende verbindingen met een maximum van 3 wachtrijen met behulp van de listen()-methode.
In een oneindige lus accepteert de server inkomende verbindingen met behulp van de accept()-methode.
Het adres van de client en het geaccepteerde socket object worden opgeslagen in de variabelen address en clientSocket respectievelijk.
Het geaccepteerde verbinding wordt afgedrukt.
Het bericht "Bedankt voor het verbinden met de server" wordt naar de client gestuurd met behulp van de send()-methode. Het bericht wordt eerst omgezet naar bytes met behulp van encode().
De verbinding met de client wordt gesloten met behulp van de close()-methode.

'''