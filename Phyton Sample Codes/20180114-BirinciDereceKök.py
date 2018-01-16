#Kullanıcı tarafından katsayıları girilen birinci dereceden denklemin köklerini bulan program

#BayMfe

import math
import sys

kontrol = True
katsayılar = []
#--------------------------------------------------------------------------

def KokBul():

    katsayılar.append(KatsayıAl())
    # (C-B)/A
    A = katsayılar[0]
    B = katsayılar[1]
    C = katsayılar[2]
    print("Katsayıları girilen denklemin kökü : {}".format(float((C-B)/A)))

def KatsayıAl():
    try:
        k_A = int(input("Lütfen A katsayısı için değer giriniz: "))
        k_B = int(input("Lütfen B katsayısı için değer giriniz: "))
        k_C = int(input("Lütfen C katsayısı için değer giriniz: "))
    except ZeroDivisionError:
        print("Lütfen sıfırdan farklı bir değer giriniz.\n")
        KokBul()
    except ValueError:
        print("Lütfen sadece tamsayı giriniz.\nKatsayılar adı üzerinde sayılardan oluşur!!!\n")
        KokBul()
    except UnboundLocalError:
        print("\n")
    if (k_A != 0 and k_B != 0 and k_C != 0):    # Katsayıların girilen değerlerin arasında sıfır olup olmadığı kontrol ediliyor
        katsayılar.append(k_A)
        katsayılar.append(k_B)
        katsayılar.append(k_C)
    else:print("Katsayı değerleri sıfır olamaz.Tekrar deneyiniz.\n"),KokBul()

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

def Cıkıs():
        print("Programımız sonlandırıldı.\nİyi Çalışmalar.")
        sys.exit()



#--------------------------------------------------------------------------
print("""

                      - Ax + B = C -
şeklindeki birinci dereceden denklemin köklerini bulan programa
                        HOŞGELDİNİZ 

""")
while kontrol == True:
    KokBul()
    Tekrar()









