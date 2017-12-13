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

def MukemmelSorgu(Tam):

    Tam.pop() #listenin son elemanını çıkarır. Listenin son elemanı kendisi olduğu için son eleman toplama işlemine dahil edilmez

    toplam=0
    for i in Tam:
        toplam += i

    if sayı == toplam:
        print("girdiğiniz sayı mükemmel sayıdır.")
    else:print("girdiğiniz sayı Mükemmel Sayı DEĞİLDİR")



while kontrol == True:

    sayı = int(input("Sayı giriniz: "))
    b_sayı = sayı
    MukemmelSorgu(TamBölen(b_sayı))


    kontrol = sayıSor()























