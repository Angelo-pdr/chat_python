import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5050))

server.listen()
client, end = server.accept()

finished = False

while not finished:
    msg = client.recv(1024).decode("UTF-8")
    if msg == 'gg':
        finished = True
    else:
        print(msg)
    client.send(input("Message: ").encode("UTF-8"))
client.close()
server.close()
