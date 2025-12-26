
import socket
import threading

host = "127.0.0.1" # localhost

port = 44444


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen()
print("Server is listening...\n")

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} has been removed ".encode("ascii"))
            break



def receive():
    while True:
        client,address = server.accept()
        print(f"Connected to {address}")

        client.send("Nickname : ".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        clients.append(client)
        nicknames.append(nickname)
        
        broadcast(f"{nickname} joined the chat".encode("ascii"))
        client.send("connected to the server...".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()






