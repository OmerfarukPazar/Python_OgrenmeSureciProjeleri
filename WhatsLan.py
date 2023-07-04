###############################################
#   ÜYE OL ---- KAYIT OL --- Şifremi Unuttum Seçenekleri Olacak 
# Üyeler Görüntülenebilecek Mesaj Atılacak 
# Kullanıcı Giriş Yaptığı Zaman Gelen Mesajlar Kullanıcı İsmi ile Gözükecek
# Mesaj Yazabilecek 
# Kullanıcı Engelleyebilecek 
# Çıkış Ekranına Dönüp Farklı Bir Kullanıcı ile Giriş Yapmayı Deneyebilecek 
# Admin Paneli 
# Şifremi unuttum : Mail Adresi isteyecek kullanıcı adı isteyecek doğruysa yeni şifre oluşturcak ve print verecek
###############################################

#ANA KATMAN 
#FONKSİYONLAR
uyeler=[]
mesajlar=[]
def uyeekleme(uyeol:tuple,uyeler:list):
    uyetel=input("Lütfen 5** *** **** Formatında Telefon Numaranızı Giriniz... ") 
    telkontrol(uyetel,uyeler)
    uyeisim=input("Lütfen Oluşturmak İstediğiniz Üye İsminizi Giriniz...")

    uyesifre=input("Lütfen Oluşturmak İstediğiniz Üye Sifrenizi Giriniz...")
    uyeol=(uyetel,uyeisim,uyesifre)
    uyeler.append(uyeol)
    print("Başarıyla Kayıt Olundu...")

def telkontrol(uyetel,uyeler):
    for sayac,veri in enumerate(uyeler):
        if  uyetel in veri[0] :
            print("Bu telefon numarası zaten kayıtlı....")
            anamenu()
    
def sifremiunuttum(uyetel1,uyeisim1):
    global uyeler
    for sayac,veri in enumerate(uyeler):
        #print(i)
        if uyetel1 == veri[0] and uyeisim1 == veri[1]:
                a = list(veri)
                a[2] =input("yeni şifreniz:  ")
                veri = tuple(a)
                uyeler[sayac]=veri
                return True                      
    print("Böyle Bir Kullanıcı Yok....")
    return False

def girisyap(giris_telno,giris_sifre):
    for sayac,veri in enumerate(uyeler):
        if giris_telno == veri[0] and giris_sifre == veri[2]:
            print("Başarıyla Giriş Yaptınız ")
            mesajlar[sayac].append()
            abc=input("mesaj yaz .... ")
            
            return True
    print("Hatalı Giriş Yaptınız ... ")
    return False
    anamenu()



def anamenu():
    print("Üye Olmak İçin [1] ********* Şifrenizi Unuttuysanız [2]********** Giriş Yapmak İçin [3]************")
    secim=input("secim: ")
    if secim =="1" :
        uyeol=()
        uyeekleme(uyeol,uyeler)
    elif secim =="2":
        print("Hatırladığınız Telefon Numaranız ve Kullanıcı Adınız ? ")
        uyetel1=input("Telefon Numaranız: ")
        uyeisim1=input("üye isminiz: ")
        sifremiunuttum(uyetel1,uyeisim1)
        print(uyeler)
    elif secim == "3":
        giris_telno=input("Telefon Numaranız : ")
        giris_sifre=input("Şifreniz :  ")
        girisyap(giris_telno,giris_sifre)


while True:
    anamenu()
    


#def sifremiunuttum(uye,)
    
#DÖNGÜ
(""" secim=input("Mesajlarınızı Görüntülemek İçin [1]**********Mesaj Yazmak İçin [2]*******")
            if secim == "2":
                mesaj_yaz = input("Mesaj Yazmak istediğiniz kullanıcının adı : ")
                for sayac2,veri2 in enumerate(uyeler):
                    if mesaj_yaz == veri2[1] :
                        mesaj=input("Mesajınız: ")
                        mesaj1=(mesaj_yaz,mesaj)
                        mesajlar.append(mesaj1)
                        input("Göndermek İstediğinize Emin Misiniz ? \n " +"Mesajınız: " + mesajlar)




            print("Mesajları oku .... vs.vs.vs.vs ")

            cikis=input("çıkış yapmak için 0 tuşlayınız ")
            if cikis =="0" :
                return True""")