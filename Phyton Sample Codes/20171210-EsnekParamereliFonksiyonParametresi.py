def toplam(*sayılar):
    toplama = 0
    for topla in sayılar:
        toplama += topla
    return toplama


def sayıSor():

    a = input("Yeni sayı eklemek istiyorsanız (Y), İşlemi tamamlamak için (T) tuşlayınız: ")
    if a ==  "Y":
       return True
    elif a ==  "y":
       return True
    elif a == "T":
       return False
    elif a == "t":
       return False
    else:
        print("Yanlış giriş yaptınız.\nTekrar giriniz")
        sayıSor()

print("""
Toplama İşlemini fonksiyonda esnek sayılar kullanarak 
işlem yapmayı amaçlayan programımıza hoşgeldiniz...

                 *******************
""")

kontrol = True
sayı_listesi = []

while kontrol == True:
    sayı_listesi.append(int(input("Sayı giriniz:")))
    kontrol= sayıSor()
print("Girmiş olduğunuz sayıların toplamı:",toplam(*sayı_listesi))


