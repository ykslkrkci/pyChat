import socket,threading,sys,os

host = input("Host : ")  # ! Sunucu ile aynı host girilmeli
if not host:
    host = "localhost"

port = input("Port : ") # ! Sunucu ile aynı port girilmeli 
if not port:
    port = 4444
else:
    port = int(port)

s = socket.socket()
s.connect((host,port)) # s.bind'den farklı olarak s.connect() ile bağlanmak istediğimizi belli ettik
print(s.recv(1024).decode()) # Sunucdan gelen hoş geldin mesajını ilettik
while 1:
    username = input("Kullanıcı adınızı girin ! : ")
    if username:break
    else:print("Username boş olamaz ? \n")
while 1:
    sifre = input("Şifrenizi girin ! : ")
    if sifre:
        bilgiler = username+"|*|"+sifre # Sunucuya bilgileri username|*|pass olarak atıyoruz , öyle işenmesini ayarlamıştık
        s.sendall(bilgiler.encode()) # encode edip yolluyoruz
        break
    else:print("Şifre nasıl boş olabilir ? \n")
cevap = s.recv(1024).decode() # sunucuda 1 ve 0 yollamıştık hatırlıyorsanız . Burada onları alıyoruz
if cevap == "0": # eğer sunucudan dönen cevap 0 ise çıkış yapıyoruz
    print("Bilgiler kabul edilmedi !")
    input()
    sys.exit()
elif cevap == "1": # gelen cevap 1' ise devam ediyoruz
    print("Giriş başarılı . Hoşgeldiniz !")

else: # Sunucu bilinmeyen bir cevap veriyorsa gine çıkıyoruz :)
    print("Sunucu bilinmeyen bir cevap verdi \n"+cevap)
    sys.exit(input())



def cevap():
    while 1:
        yanit = s.recv(1024) # Sunucudan gelen veriyi yanit'a atadık
        print("\033[31mSunucu : \033[0m"+yanit.decode()) # Sunucunun cevabını ekrana yazdık
threading.Thread(target=cevap).start() # Threading ile bu eylemi arkaplanda sürekli yapmasını sağlıyoruz
while 1: # Cevap vereceğiz bunun için döngüye aldık
    yolla = input() # input'umuzu yollaya'ya attık
    s.sendall(yolla.encode()) # yollayı sunucya yolladık :)