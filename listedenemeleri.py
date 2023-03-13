kullanicilar=[]

while True:
    
    secim=input("""\n*****Kullanıcı Ekleme ====>  1 
*****Kullanıcıları Göster ====>  2   
*****Kullanıcı Sil ====>  3  \n""")

    if secim=="1":
        kullanicigirisi=input("Kullanıcı Adı: ")
        kullanicilar.append(kullanicigirisi) 
        print(kullanicilar)
    if secim=="2":
        quit()
    #if secim==3:
    #else :

