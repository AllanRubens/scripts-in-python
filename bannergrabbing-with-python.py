import socket

ip = raw_input("Digite o IP:")
porta = input("Digite a porta:")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip,porta))
banner = meusocket.recv(1024)
print banner