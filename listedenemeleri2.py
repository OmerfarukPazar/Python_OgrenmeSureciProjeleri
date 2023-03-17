#memory space
kullanicilar=[]
giris=input("\nGiriş yapmak için herhangi bir tuşa basınız...")
menu= """\nKullanıcı Ekleme [1]
Kullanıcı Silme [2]
Kullanıcı Listesini Görüntüle [3]
Çıkış [4]"""

def kullaniciekleme(kullaniciekle,kullanicilar):
    if eklemekontrol(kullaniciekle,kullanicilar):
        print("Kullanıcı Zaten Var....")
    else:
        kullanicilar.append(kullaniciekle)
        print("Kullanıcı Eklendi ...")
        
    
def eklemekontrol(kullaniciekle,kullanicilar):
    if kullaniciekle in kullanicilar:
        return True
    else:
        return False

def silmekontrol(kullanicisil,kullanicilar):
    if kullanicisil in kullanicilar:
        return True
    else:
        return False

def kullanicisilme(kullanicisil,kullanicilar):
    if silmekontrol(kullanicisil,kullanicilar):
        kullanicilar.remove(kullanicisil)
        print("kullanici silindi..")
    else :
        print("Hatalı Kullanıcı Girişi Yaptınız..")
""" if kullanicisil is not  kullanicilar:
            print("hatalı kullanıcı girişi yaptınız..")
            kullanicisilme()  """


def kullanicilistesi(kullanicilar):
    for i in kullanicilar:
        print(i)


def anamenu():
    print(menu)
    secim=input("yapılmak istenen işlem:  ")

    if secim=="1":
        kullaniciekle=input("eklenecek kullanıcı ismi: ")
        kullaniciekleme(kullaniciekle,kullanicilar)
        input("\nAnamenüye dönmek için enter'a basınız..")
        
    elif secim=="2":
        for i in kullanicilar:
            print(i)
        kullanicisil=input("\nSilinmek istenen kullanıcının adı: ")
        kullanicisilme(kullanicisil,kullanicilar)
        input("\nAnamenüye dönmek için enter'a basınız..")

    elif secim=="3":
        kullanicilistesi(kullanicilar)
        input("\nAnamenüye dönmek için enter'a basınız..")
    
    elif secim =="4":
        print("\nBaşarıyla Çıkış Yaptınız....")
        quit()
    else:
        print("\n************ Hatalı Giriş Yaptınız...")
        input("Tekrar menüye dönmek için enter'a basınız")


while True:

    anamenu()

    