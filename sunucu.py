kullanici_adlari = ["raif","yuksel","personanongrata"]
sifreler = ["123"]
liste = []
import socket,threading,sys
host = input("HOST : ") # hangi host'da açılmasını istediğini sorduk 
if not host:
    host = "localhost" # eğer enter'ile "" boş geçilirse localhost'da çalışacak

port = input("Port : ") # hangi port'da açılmasını istediğini sorduk
if not port:
    port = 4444 #port değeri boş ise 4444 'de açılacak
else:
    port = int(port) # str to int' yapıyoruz ki hata vermesin bize :)

s = socket.socket() # Default olarak socket.AF_INET,socket.SOCK_STREAM değeri veriliyor. Bunları baştan yazmaya gerek yok
s.bind((host,port)) # host'u ve port'u dinlemeye aldığımızı belirtiyoruz

s.listen(1) # Sadece 1 kişinin bağlanmasını isteğimizi belirttik # ** Birden fazla kişi ile konuşurken problem çıkıyor :)

def devam():
    liste.append(adres)
    c.send("Chat'e hoşgeldin".encode()) # Clien'a Chat'e Hoşgeldin mesajını ilettik
    bilgiler = c.recv(1024).decode()    # Client bize kullanıcı adı ve şifre yollamış oluyor bu veri ile 
    print("Şifre alındı !") # Şifreyi aldığımızı belirttik
    bilgiler = bilgiler.split("|*|") # kullanıcı adı bize username|*|password olarak geldiği için |*|'leri silerek bilgileri liste yapıyoruz
    print(bilgiler) # Bilgileri ekranımıza yazdık 
    if bilgiler[0] in kullanici_adlari and bilgiler[1] in sifreler: # eğer bilgiler listesinin ilk elemanı kullanici_adlari listesinin içindeyse VE bilgiler listenin ilk elemanı sifreler listesinin içindeyse:
            c.sendall("1".encode()) # c (c bizim client'ımız oluyor) 'ye mesaj at (mesaj = 1) ## Client bunu yorumlayacak eğer c == "0"'a exit verecek
    else:c.sendall("0".encode()) # değilse (c nin verdiği bilgiler bizim listeler ile uyuşmuyorsa) C'te "0" meesajını at

    def cevap(): # Threading ile açacağımız için arkaplanda sürekli mesaj bekleyecek , mesaj gelirse hemen ekrana yazacak
        while 1:
            data = c.recv(1024).decode() # C'den gelen veriyi 1 mb halinde aldık , byte halinden string'e çevirdik
            if data: # eğer mesaj varsa :
                print("\033[32m"+bilgiler[0]+" : \033[0m"+data) # ekrana mesajı yazdık [username + mesaj]
                
    threading.Thread(target=cevap).start() # Bize gelecek olan verileri arkaplanda almaya başldık böylece diğer işlerimize burnunu sokmayacak
    
    
    while 1: # mesaj gönderceğiz , sunucu kapanmasın diye sürekli döngüye aldık
        mesaj = input() # input ile yollayacak mesajı aldık
        if mesaj == "q": # Eğer mesaj q ise :
            c.sendall("0".encode()) # Client'a "0"'ı ilettik böylece ona da exit verdireceğiz
            s.close()        # sunucu'yu kapattık
            sys.exit()        # sys'e exit verdik
        
        c.sendall(mesaj.encode()) # input ile aldığımız mesajı Client'a ilettik :)


 
c , adres = s.accept() # o C'ler buydu işte :) c ile client'ı adres ile sunucu adresini aldık
devam()

# Önemli not : Sunucu ile Client arasına başka bir Client girerse o girmeye çalışan kişi boş bekleyecektir :)
    
