import socket
import sys 
import select

#serverName = 'localhost'
serverName = input("Jepe emrin e serverit:")
#serverPort = 12000
Port = input("Jepeni vleren e portit:")
serverPort = int(Port)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverName,serverPort))
while True:
    print("============================================================================")
    var=input("Zgjedhni njeren nga metodat: \n IPADRESA\n NUMRIIPORTIT\n BASHKETINGELLORE\n PRINTIMI\n EMRIIKOMPJUTERIT\n KOHA\n LOJA\n FIBONACCI\n KONVERTIMI\n" +" Por ne rast se keni perfunduar mund te shtypni enter per mbyllje programi\n ")
    print("============================================================================")
    var=var.strip() 
    if len(var) > 128:
        print("Kerkese eshte qe metoda te jete ne mes intervalit 1-128 karaktere")
        continue
    if not var:
        print("Shenoni njeren nga metodat!")
        continue
    if var == "enter":
        s.close()
        break
    s.sendall(str.encode(var))
    data = s.recv(1024)
    data = data.decode('utf-8')
    print(data)