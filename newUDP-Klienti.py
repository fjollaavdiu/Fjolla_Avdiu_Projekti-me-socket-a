import socket
import sys 
import select

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
#serverName = 'localhost';
serverName = input("Jepe emrin e serverit:")
#serverPort = 12000;
Port = input("Shenoni portin:")
serverPort = int(Port)
addr = (serverName, serverPort)

while True:
    print("============================================================================")
    var=input("Zgjedhni njeren nga metodat: \n IPADRESA\n NUMRIIPORTIT\n BASHKETINGELLORE\n PRINTIMI\n EMRIIKOMPJUTERIT\n KOHA\n LOJA\n FIBONACCI\n KONVERTIMI\n ZANORET\n PRIME\n" +" Por ne rast se keni perfunduar mund te shtypni enter per mbyllje programi\n ")
    print("============================================================================")
    if not var:
        print("Shenoni njeren nga metodat!")
        continue
    if var == "enter":
        client_socket.close()
        break
    client_socket.sendto(var.encode(),addr)
    try:
        data, server = client_socket.recvfrom(1024)
        data = data.decode('utf-8')
        print(data)
    except socket.timeout:
        print('REQUEST TIMED OUT')
print("============================================================================")
    