#memory space
kullanicilar=[]
giris=input("giriş yapmak için herhangi bir tuşa basınız...")
menu= """\nKullanıcı Ekleme [1]
Kullanıcı Silme [2]
Kullanıcı Listesini Görüntüle [3]
Çıkış [4]"""
    
def kullaniciekleme(kullaniciekle,kullanicilar):
    kullanicilar.append(kullaniciekle)
    

def kullanicisilme(kullanicisil,kullanicilar):
    kullanicilar.remove(kullanicisil)
    """ if kullanicisil is not  kullanicilar:
        print("hatalı kullanıcı girişi yaptınız..")
        kullanicisilme()
    else :
        pass """


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
        input("anamenüye dönmek için enter'a basınız..")
        
    if secim=="2":
        for i in kullanicilar:
            print(i)
        kullanicisil=input("\nSilinmek istenen kullanıcının adı: ")
        kullanicisilme(kullanicisil,kullanicilar)
        print("kullanici silindi..")
        input("anamenüye dönmek için enter'a basınız..")

    if secim=="3":
        kullanicilistesi(kullanicilar)
        input("anamenüye dönmek için enter'a basınız..")
    
    if secim =="4":
        quit()
    else:
        print("\n************ Hatalı Giriş Yaptınız...")
        input("Tekrar menüye dönmek için enter'a basınız")


while True:

    anamenu()
    



    """ print(menu)    
    secim=input("yapılmak istenen işlem ")

    if secim=="1":
        kullaniciekle=input("eklenecek kullanıcı ismi: ")
        kullaniciekleme(kullaniciekle,kullanicilar)
        print(kullanicilar)
        
    if secim=="2":
        kullanicisil=input("silinmek istenen kullanıcının adı: ")
        kullanicisilme(kullanicisil,kullanicilar)
        print(kullanicilar)

    if secim=="3":
        kullanicilistesi(kullanicilar)
    
    if secim =="4":
        quit()

    else:
        print("hatalı tuşlama yaptınız...") """