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
    uyeisim=input("Lütfen Oluşturmak İstediğiniz Üye İsminizi Giriniz...")
    uyesifre=input("Lütfen Oluşturmak İstediğiniz Üye Sifrenizi Giriniz...")
    uyeol=(uyemail,uyeisim,uyesifre)
    uyeler.append(uyeol)
    print("Başarıyla Kayıt Olundu...")

def sifremiunuttumkontrol(uyemail1,uyeisim1):
    global uyeler
    
    for i in uyeler:
        #print(i)
        if uyemail1 == i[0] and uyeisim1 == i[1]:
            a = list(i)
            a[2] =input("yeni şifreniz:  ")
            i = tuple(a)                        #  ÜYELERE YENİ İ VERİSİNİ GEÇİREMEDİM  (İ DÜZENLENDİ)
            return True  
    print("Böyle Bir Kullanıcı Yok....")
    return False
        

#def sifremiunuttum():

    



while True:
    secim=input("secim: ")
    if secim =="1" :
        uyeol=input()
        uyeekleme(uyeol,uyeler)
    elif secim =="2":
        uyemail1=input("mail adresiniz: ")
        uyeisim1=input("üye isminiz: ")
        sifremiunuttumkontrol(uyemail1,uyeisim1)
        print(uyeler)
    


#def sifremiunuttum(uye,)
    
#DÖNGÜ