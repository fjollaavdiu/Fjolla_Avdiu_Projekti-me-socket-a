import socket
from datetime import datetime
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 12000))

#funksioni per llogaritjen e fibonnacit
def FIBONACCI(n):  
   if n <= 1:
       return n
   else:
       return(FIBONACCI(n-1) + FIBONACCI(n-2))

#funksioni per konvertim 
def KONVERTIMI(opt,vlera):
    nr = 0
    try:
        nr = float(vlera)
    except:
        return "gabim".encode()
    if opt=="KilowattToHorsepower":
        return str(nr*1.341)
    elif opt=="HorsepowerToKilowatt":
        return str(nr/1.341)
    elif opt=="DegreesToRadians":
        return str(nr*3.14/180)
    elif opt=="RadiansToDegrees":
        return str(nr*180/3.14)
    elif opt=="GallonsToLiters":
        return str(nr*3.785)
    elif opt=="LitersToGallons":
        return str(nr/3.785)
    else:
        return "gabim".encode()
        return (nr*2.2)

#MAIN FUNCTION 
def METODAT(metoda_arr,lidhja,addr):
    if(metoda_arr[0]=='IPADRESA'):
        lidhja.send(str.encode(" KJO ESHTE IP E KLIENTIT:"+addr[0]))

    elif(metoda_arr[0]=='NUMRIIPORTIT'):
       lidhja.send(str.encode("KLIENTI SHFRYTEZON KETE PORT:"+str(addr[1])))

    elif(metoda_arr[0]=='BASHKETINGELLORE'):
        mesazhi = ""
        string = mesazhi.strip()
        bashketingellore = set("BCDFGHJKLMNPQRSTVXZWbcdfghjklmnpqrstv")
        try: 
            if not string:
                return ("gabim")
            else: 
                nrbashketingelloreve = 0
                for char in string:
                    if char in bashketingellore: 
                        nrbashketingelloreve = nrbashketingelloreve+1
                    teksti= "Teksti ka "  + str(nrbashketingelloreve)+ "bashketingellore"
                    return teksti.encode()
        except IndexError:
            print("Mund te paraqitni ndonje fjali tjeter")


    elif(metoda_arr[0]=='PRINTIMI'):
        try:
            stringu=""
            stringu=str.join(" " , metoda_arr[1:])
            lidhja.send(str.encode("DEKLARO FJALINE PER PRINTIM"+stringu))
        except IndexError:
            print("Mund te paraqitni ndonje fjali tjeter")

            
    elif(metoda_arr[0]=='EMRIIKOMPJUTERIT'):
        try:
            hostname=socket.gethostname()
            lidhja.send( str.encode("EMRI I KOPJUTERIT "+hostname))
        except error:
            print("Emri i kompjuterit fatkeqesisht nuk u")

    elif(metoda_arr[0]=='KOHA'):
        time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lidhja.send(str.encode(time))

    elif(metoda_arr[0]=='LOJA'):
        srand= ''
        for x in range(0,7):
            rand= random.randint(1,49) 
            randString = str(rand) + " " 
            srand += randString           
        lidhja.send(str.encode(srand))

    elif(metoda_arr[0]=='FIBONACCI'):
        try:
            n=FIBONACCI(int(metoda_arr[1]))
            lidhja.send(str.encode(str(n)))
        except IndexError:
            lidhja.send(str.encode("Ju lutem shenoni nje shifer pas kerkeses FIBONACCI"))
        except ValueError:
            lidhja.send(str.encode("Ju lutem shenoni nje shifer pas kerkeses FIBONACCI"))

    elif(metoda_arr[0]=='KONVERTIMI'):
        try:
            s=metoda_arr[1]
            n=float(metoda_arr[2])
            lidhja.send(str.encode(str(KONVERTIMI((opt,vlera))))
    except IndexError:
            lidhja.send(str.encode("Ju lutem shenoni kerkesen qe deshironi ta konvertoni"))
        except ValueError:
            lidhja.send(str.encode("Ju lutem shenoni se pari kerkesen pastaj shifren \n"))
    
 
while True:
    kerkesa, addr = server_socket.recvfrom(1024)
    kerkesa = kerkesa.decode('utf-8')
    kerkesaVarg= kerkesa.split()
    perpunimi_kerkeses(kerkesaVarg,server_socket,addr)
    