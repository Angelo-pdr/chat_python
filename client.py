import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5050))

finished = False
print("Digite gg para finalizar o chat")

while not finished:
    client.send(input("Mensagem: ").encode("UTF-8"))
    msg = client.recv(1024).decode("UTF-8")
    if msg == 'gg':
        finished = True
    else:
        print(msg)

client.close()
