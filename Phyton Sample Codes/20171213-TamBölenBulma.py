def sayıSor():

    a = input("Yeni sayı denemek istiyorsanız (Y), İşlemi tamamlamak için (T) tuşlayınız: ")
    if a ==  ("y") :
       return True
    elif a ==  ("Y") :
       return True

    elif a == ("T"):
       return False
    elif a == ("t"):
       return False
    else:
        print("Yanlış giriş yaptınız.\nTekrar giriniz")
        sayıSor()


def TamBölen(sayı):
    Tam=[]

    for i in range(1,sayı+1):
        if (sayı % i == 0):
            Tam.append(i)
    return Tam
kontrol = True

while kontrol == True:

    sayı = int(input("Sayı giriniz: "))

    print(TamBölen(sayı))

    kontrol = sayıSor()























