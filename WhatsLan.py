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
    uyemail=input("Lütfen Mail Adresinizi Giriniz...") 
    mailkontrol(uyemail,uyeler)
    uyeisim=input("Lütfen Oluşturmak İstediğiniz Üye İsminizi Giriniz...")

    uyesifre=input("Lütfen Oluşturmak İstediğiniz Üye Sifrenizi Giriniz...")
    uyeol=(uyemail,uyeisim,uyesifre)
    uyeler.append(uyeol)
    print("Başarıyla Kayıt Olundu...")

def mailkontrol(uyemail,uyeler):
    for sayac,veri in enumerate(uyeler):
        if  uyemail in veri[0] :
            print("Bu mail adresi zaten kayıtlı....")
            anamenu()
    
def sifremiunuttum(uyemail1,uyeisim1):
    global uyeler
    for sayac,veri in enumerate(uyeler):
        #print(i)
        if uyemail1 == veri[0] and uyeisim1 == veri[1]:
                a = list(veri)
                a[2] =input("yeni şifreniz:  ")
                veri = tuple(a)
                uyeler[sayac]=veri
                return True                      
    print("Böyle Bir Kullanıcı Yok....")
    return False

def girisyap(giris_kullanıcıadı,giris_sifre):
    for sayac,veri in enumerate(uyeler):
        if giris_kullanıcıadı == veri[1] and giris_sifre == veri[2]:
            print("Başarıyla Giriş Yaptınız ")
            secim=input("Mesajlarınızı Görüntülemek İçin [1]**********Mesaj Yazmak İçin [2]*******")
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
                return True
        return True

    print("Hatalı Giriş Yaptınız ... ")
    anamenu()



def anamenu():
    print("Üye Olmak İçin [1] ********* Şifrenizi Unuttuysanız [2]********** Giriş Yapmak İçin [3]************")
    secim=input("secim: ")
    if secim =="1" :
        uyeol=()
        uyeekleme(uyeol,uyeler)
    elif secim =="2":
        print("Hatırladığınız Mail Adresiniz ve Kullanıcı Adınız ? ")
        uyemail1=input("mail adresiniz: ")
        uyeisim1=input("üye isminiz: ")
        sifremiunuttum(uyemail1,uyeisim1)
        print(uyeler)
    elif secim == "3":
        giris_kullanıcıadı=input("Kullanıcı Adınız : ")
        giris_sifre=input("Şifreniz :  ")
        girisyap(giris_kullanıcıadı,giris_sifre)


while True:
    anamenu()
    


#def sifremiunuttum(uye,)
    
#DÖNGÜ