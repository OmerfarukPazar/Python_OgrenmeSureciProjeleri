liste=[]

def menu():
    print("Sınıf Öğrenci Bilgi Sistemine Hoşgeldiniz...")
    print("Lütfen Yapmak İstediğiniz İşlemi Seçiniz ...")
    print("""-----------------------------------
    [1] Öğrenci Kayıt
    [2] Sınıf Listesi Sorgulama
    [3] Çıkış
------------------------------------""")
    
def ogrencikayit(ogrenci,liste):

    liste += [ogrenci]
    ogrencitercih=input("""------------------------------------------
                        Menüye Dönmek İçin 0 Tuşlayınız     
                        Uygulamadan Çıkş Yapmak İçin 1 Tuşlayınız    
                        ------------------------------------------""")
    if ogrencitercih == "0":
        return True
    elif ogrencitercih == "1":
        quit()
    else :
        print("Hatalı Tuşlama Yaptınız...")
    
   

def listegetir(liste):

    print(liste)

    tercihliste=input("""------------------------------------------
                        Menüye Dönmek İçin 0 Tuşlayınız     
                        Uygulamadan Çıkş Yapmak İçin 1 Tuşlayınız    
                        ------------------------------------------""")
    if tercihliste == "0" :
        pass
    elif tercihliste == "1" :
        quit()
    else :
        print("Hatalı Tuşlama Yaptınız... ")

while True :

    menu()
    
    tercihmenu=input("Seçiminiz : ")

    if  tercihmenu == "1":
        ogrenci=input("Eklemek İstediğiniz Öğrencinin Adı Soyadı :")
        ogrencikayit(ogrenci,liste)
    elif tercihmenu == "2":
        listegetir(liste)
    elif tercihmenu == "3" :
        quit()
    else:
        print("Hatalı Tuşlama Yaptınız....")   
    
    
    
    

