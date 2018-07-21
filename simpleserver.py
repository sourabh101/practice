import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = socket.gethostname()
ip = socket.gethostbyname(name)
port = 1235
address = (ip, port)
server.bind(address)
server.listen(1)
print("Started listening on ip: {}, port: {}".format(ip, port))

client, addr = server.accept()
print("Got a connection from ip: {}, port: {}".format(addr[0], addr[1]))

while True:
    data = client.recv(1024)
    print("Data: {}".format(data))

    if data == "Hello server".encode():
        client.send("Hello client".encode())
        print("Hello client")
    elif data == "Disconnect".encode():
        client.send("Goodbye".encode())
        print("Good bye")
        client.close()
        break
    else:
        client.send("Invalid data".encode())
        print("invalid")
