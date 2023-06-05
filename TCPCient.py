import socket

# Een socket object maken voor de client
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Het verkrijgen van de hostnaam van de huidige machine
host = socket.gethostname()
# De poort waarmee de client verbinding maakt
port = 444

# Verbinding maken met de server via het opgegeven hostadres en poort
clientSocket.connect((host, port))

# Het ontvangen van gegevens van de server
message = clientSocket.recv(1024)

# Sluiten van de verbinding met de server
clientSocket.close()

# Het afdrukken van het ontvangen bericht
print(message.decode('ascii'))


'''
De code maakt gebruik van de socket module om een client te maken die verbinding maakt met een server.
Er wordt een socket object gemaakt voor de client met het adresfamilie AF_INET en het sockettype SOCK_STREAM.
De hostnaam wordt verkregen met behulp van socket.gethostname() en opgeslagen in de variabele host.
De poort wordt ingesteld op 444 en opgeslagen in de variabele port.
De client maakt verbinding met de server door het socket object te koppelen aan het hostadres en de poort met behulp van de connect()-methode.
De client ontvangt gegevens van de server met behulp van de recv()-methode. Het maximale aantal bytes dat wordt ontvangen is 1024.
Na het ontvangen van de gegevens wordt de verbinding met de server gesloten met behulp van de close()-methode.
Het ontvangen bericht wordt afgedrukt nadat het is gedecodeerd met behulp van decode('ascii'). Dit gaat ervan uit dat het bericht ASCII-gecodeerd is.

'''
