import socket
import sys
from _thread import *
from datetime import datetime
import random


host = ''
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverSocket.bind((host, serverPort))
except socket.error as errori:
    print(str(errori))

print('Serveri u startua ne localhost:'+str(serverPort))
serverSocket.listen(10)
print('Serveri eshte i gatshem te pranoj kerkesa')

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

    elif (metoda_arr[0]=='EMRIIKOMPJUTERIT'):
        try:
            mesazhi = socket.gethostbyaddr("localhost")
            lidhja.send(("Emri i klientit është: " + str(mesazhi)).encode("UTF-8"))
        except Exception:
            lidhja.send("Nuk lejohet kjo informate!")        

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
        S1="Konvertimet:"
        S2="Konvertimet"
        try:
            opt=metoda_arr[1]
            vlera=float(metoda_arr[2])
            # lidhja.send(str.encode(str(KONVERTIMI((opt,vlera)))))
        except IndexError:
            lidhja.send(str.encode("Ju lutem shenoni kerkesen qe deshironi ta konvertoni"+S1+S2))
        except ValueError:
            lidhja.send(str.encode("Ju lutem shenoni se pari kerkesen pastaj shifren"+S1+S2))

    elif(metoda_arr[0]=='ZANORE'):
        try:
            s=""
            s=s.join(metoda_arr[1:])         
            count = 0
            zanoret = set("aeiouy\u00EB")
            for letter in s:             
                if letter in zanoret:    
                    count += 1
            lidhja.send(str.encode("Teksti i pranuar përmban "+ str(count) +" zanore"))
        except IndexError:
            lidhja.send(str.encode("Shenoni nje fjali pas kerkeses ZANORE!"))
    
    
    elif(metoda_arr[0]=='PRIME'):
        try:
            n = int(metoda_arr[1])
            if is_prime(n):
                lidhja.send(str.encode("Numri " + str(n) + " eshte numer i thjeshte!"))
            else:
                lidhja.send(str.encode("Numri " + str(n) + " nuk eshte numer i thjeshte!"))
        except IndexError:
            lidhja.send(str.encode("Shenoni nje numer pas kerkeses PRIME!"))
        except ValueError:
            lidhja.send(str.encode("Shenoni nje numer te plote pas kerkeses PRIME!"))

    else:
        print("JU LUTEM SHENONI NJEREN NGA KERKESAT")
  
def klient_thread(lidhja,addr):
    while True:
        try:
            data=lidhja.recv(1024)
            kerkesa = data.decode('utf-8')
            metoda_arr = kerkesa.split()
            try:
                METODAT(metoda_arr,lidhja,addr)
            except IndexError:
                lidhja.send(str.encode("Kerkesa nuk eshte valide!"))
        except OSError:
            lidhja.close()
    lidhja.close()


while True: 
    lidhjaSocket, addr = serverSocket.accept()
    print('Klienti u lidh ne serverin %s me port %s' % addr)
    start_new_thread(klient_thread,(lidhjaSocket,addr,))




