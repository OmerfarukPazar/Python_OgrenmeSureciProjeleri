#memory space
kullanicilar=[]
giris=input("\nGiriş yapmak için herhangi bir tuşa basınız...")
menu= """\nKullanıcı Ekleme [1]
Kullanıcı Silme [2]
Kullanıcı Listesini Görüntüle [3]
Çıkış [4]"""
    
def kullaniciekleme(kullaniciekle,kullanicilar):
    kullanicilar.append(kullaniciekle)
    
# deneme yarım kaldı def kontrol(kullaniciekleme)   

def kullanicisilme(kullanicisil,kullanicilar):
    kullanicilar.remove(kullanicisil)
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
        print(kullanicilar)
        input("\nAnamenüye dönmek için enter'a basınız..")
        
    elif secim=="2":
        for i in kullanicilar:
            print(i)
        kullanicisil=input("\nSilinmek istenen kullanıcının adı: ")
        kullanicisilme(kullanicisil,kullanicilar)
        print("kullanici silindi..")
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

    