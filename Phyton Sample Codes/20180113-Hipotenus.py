# 2 dik kenarı verilen üçgenin hipotenüsünü bulan program.
#BayMFE

import math
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
        dikKenarAl()
    except ZeroDivisionError:
        print("Lütfen sıfırdan farklı bir değer giriniz.\n")
        dikKenarAl()
    except UnboundLocalError:
        print("Bir hata oluştu tekrar deneyiniz.\n")
        dikKenarAl()
    if d1 == int(0):
        print("Bir hata oluştu tekrar deneyiniz.\n")
        dikKenarAl()
    elif d2 == int(0):
        print("Bir hata oluştu tekrar deneyiniz.\n")
        dikKenarAl()
    return d1,d2
def Tekrar():

    a = str(input("Yeniden denemek istiyorsanız (Y), Programı sonlandırmak için (S) tuşlayınız: "))
    if a == ("y"):
        return True
    elif a == ("Y"):
        return True

    elif a == ("S"):
        return False
    elif a == ("s"):
        return False
    else:
        print("Yanlış giriş yaptınız.\nTekrar giriniz")
        a = str("")
        Tekrar()

###################################################################################################

print("Hipotenüs hesaplama programına hoşgeldiniz.\n\n")
while kontrol == True:
    dikkenarlar = []

    dikkenarlar.append(dikKenarAl())
    hipotenus = math.sqrt(((dikkenarlar[0][0])**2)+((dikkenarlar[0][1])**2))
    print(hipotenus)
    kontrol=Tekrar()

print("Programımız sonlandırıldı.\nİyi Çalışmalar.")