
import socket
import threading

host = "127.0.0.1"  # -> use your LAN ip same as server ip
port = 44444

nickname = input("Enter your name : ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            
            if(message.startswith("Nickname")):
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("error occurred")
            client.close()
            break


def write_message():
    while True:
        try:
            message = f"{nickname}: {input('')}"
            client.send(message.encode("ascii"))
        except:
            print("server disconnected")
            client.close()
            break;


receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()
