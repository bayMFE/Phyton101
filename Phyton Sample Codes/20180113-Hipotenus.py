# 2 dik kenarı verilen üçgenin hipotenüsünü bulan program.
#BayMFE

import math
import sys
kontrol=True

###################################################################################################

def dikKenarAl():
    d1 = int(0)
    d2 = int(0)
    try:
        d1 = int(input("Lütfen 1.dik kenar uzunluğunu giriniz: "))
        d2 = int(input("Lütfen 2.dik kenar uzunluğunu giriniz: "))
    except ValueError:
        print("Lütfen sadece sayı giriniz.\n")
        d1 = int(0)
        d2 = int(0)
        Hipotenus()
    except ZeroDivisionError:
        print("Lütfen sıfırdan farklı bir değer giriniz.\n")
        Hipotenus()
    except UnboundLocalError:
        print("Bir hata oluştu tekrar deneyiniz.\n")
        Hipotenus()
    return d1,d2


def Tekrar():

    a = str(input("Yeniden denemek istiyorsanız (Y), Programı sonlandırmak için (S) tuşlayınız: "))
    if a == ("y"):
        kontrol = True
    elif a == ("Y"):
        kontrol = True

    elif a == ("S"):
        Cıkıs()
    elif a == ("s"):
        Cıkıs()
    else:
        print("Yanlış giriş yaptınız.\nTekrar giriniz")
        a = str("z")
        Tekrar()

def Hipotenus():
    dikkenarlar = []

    dikkenarlar.append(dikKenarAl())
    hipotenus = math.sqrt(((dikkenarlar[0][0]) ** 2) + ((dikkenarlar[0][1]) ** 2))
    if hipotenus != int(0):
        print(hipotenus)



###################################################################################################

print("Hipotenüs hesaplama programına hoşgeldiniz.\n\n")
while kontrol == True:
    Hipotenus()
    Tekrar()

