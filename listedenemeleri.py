""" kullanicilar=[]

while True:
    
    secim=input(\n*****Kullanıcı Ekleme ====>  1 
*****Kullanıcıları Göster ====>  2   
*****Kullanıcı Sil ====>  3  \n)

    if secim=="1":
        kullanicigirisi=input("Kullanıcı Adı: ")
        kullanicilar.append(kullanicigirisi) 
        print(kullanicilar)
    if secim=="2":
        quit()
    #if secim==3:
    #else : """
#########################################################################################
#listedenemeleri2 programı için listeden kullanıcı eşleştrime denemlerini burda yapacağım
#########################################################################################


#başarısız deneme
""" kullanicilar=["mali","ayşeinci"]
kullanicilar2={}
kullanicilar.append(kullanicilar2)
if kullanicilar.__contains__(kullanicilar2):
    for i in kullanicilar:
        print(i) """


#başarısız deneme
""" a=[]
kullaniciadi=input("kullanıcı adı giriniz: ")
sifre=input("sifre giriniz : ")

dosya=open("dosya.txt","a")
dosya.write(kullaniciadi+" "+sifre+"\n")
okuma=open("dosya.txt","r")
a=okuma.readlines()
print(a)

for line in a :
    if kullaniciadi and sifre in line:
        print("deneme başarılı.")
 """
#başarısız deneme
""" b=["ömer"]
a=input("yazınız: ")

if str(a.__contains__(b)) :
    print("wow")
 """


#şifreleme yöntemi ile dosyaya kaydetme denemesi (başarısız) 
""" import hashlib

isim=input("isim giriniz: ")
sifre=input("sifre giriniz: ")
isim_encode=isim.encode()
sifre_encode=sifre.encode()
isim_hash= hashlib.md5(isim_encode).hexdigest()
sifre_hash= hashlib.md5(sifre_encode).hexdigest() """

#dosyaya her seferinde kullanıcı eklememek için burayı yorum aldım 
""" dosya=open("isim.txt","a")
dosya.write(isim_hash+"\n") """
""" okuma=open("isim.txt","r")
stored_username,stored_pwd=okuma.read().split("\n") """ #burdaki okuma kısmında sıkıntı var

#dosyaya her seferinde kullanıcı eklememek için burayı yorum aldım 
""" dosya2=open("sifre.txt","a")
dosya2.write(sifre_hash+"\n") """
""" okuma2=open("sifre.txt","r")
stored_pwd=okuma2.read().split("\n") """ # ayrıca burdaki okuma kısmında da sıkıntı var


#1. Yöntem birden fazla okuma yapamıyor 
""" if isim_encode == stored_username and sifre_encode==stored_pwd :
         print("Logged in Successfully!")
else:
         print("Login failed! \n") """
         
#2.Yöntem çalışyor ancak farklı bir isim girildiği zaman error veremıyor 
"""
a=0
b=0
for x in stored_username:
    if stored_username==x:
        a=+a
    else:
        pass
print(a)
for i in stored_pwd:
    if sifre_hash==i:
        b=+b
    else:
        pass
if a + b > 0 :
    print("hoşgeldiniz")
else :
    print("hatalı giriş yaptınız") """

#id denemesi 

""" isimler=[]
def isimekleme(isimekle,isimler):
    isimid=id(isimekle)
    isimler.append(isimid)
    
while True:
    isimekle=input("yazınız..")
    isimekleme(isimekle,isimler)  
 """

 

