
sayi1=float(input("0-23 Aralığında Sayı Giriniz: "))

if sayi1 >= 24  :
    print("Lütfen İstenilen Aralıkta Sayı Giriniz ")

    
else :
    sayi2= float(input("Lütfen Aynı Aralıklarda İkinci Bir Sayı Giriniz:"))

    if sayi2 < 24 :
        print("==================================" , "\n" , "Lütfen Yapmak İstediğiniz İşlemi Rakam Olarak Giriniz", "\n" , "==============================" ,"\n" ,"Gerçekleştirebileceğiniz İşlemler: 1) Çarpma 2) Bölme 3) Toplama 4)Çıkarma  ")
        islem=int(input())
        if islem == 1:
            sayi3=(sayi1) * (sayi2)
            print("İşlem Sonucunuz : ", str(sayi3))
        elif islem == 2:
            print("İşlem Sonucunuz : ", (sayi1) / (sayi2))
        elif islem == 3 : 
            print("İşlem Sonucunuz : ", (sayi1) + (sayi2))
        elif islem == 4:
            print("İşlem Sonucunuz : ", (sayi1) - (sayi2))

        
#commitdenemesi
#mali
