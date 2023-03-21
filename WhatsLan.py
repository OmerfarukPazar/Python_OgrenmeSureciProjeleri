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


def anamenu():
    print("Üye Olmak İçin [1] ********* Şifrenizi Unuttuysanız [2]**********")
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


while True:
    anamenu()
    


#def sifremiunuttum(uye,)
    
#DÖNGÜ