#Developed by bayMFE

import math
import sys

global A,B,C,k1,k2
Kontrol = True
#-------------------------------- FUNCTIONS --------------------------------



def sayıAl():
    global A, B, C

    A= int(0)
    B= int(0)
    C= int(0)
    try:
        A = int(input("Lütfen A katsayısını giriniz: "))
        B = int(input("Lütfen B katsayısını giriniz: "))
        C = int(input("Lütfen C katsayısını giriniz: "))
    except ValueError:
        print("Lütfen sadece tamsayı giriniz.\nKatsayılar adı üzerinde sayılardan oluşur!!!\n")
        return 1 # hata kodu gönderiyorum

    return 0 # Hatasız sayı alındı. Kontrole gönder programa devam et

def kontrol(hata_kodu):
    if hata_kodu == 0:
        pass
        #print("Giriş doğru")
    elif hata_kodu == 1:
        print("Tekrar deneyiniz...\n\n")
        sayıAl()

def KokBul():
    global A, B, C, k1, k2
    k1 = int(0)
    k2 = int(0)
    delta = (B*B)-(4*A*C)

    if (delta > 0) :
         k1= (((B**2) - math.sqrt(delta)) / (2*A))
         k2= (((B**2) + math.sqrt(delta)) / (2*A))
         KokYaz()

    elif (delta == 0):
        k1 = (-B) / (2*A)
        k2 = k1
        KokYaz()

    else : print("Denklemin kökleri imajinerdir.")

def KokYaz():
    global k1,k2
    print("1.Kök: {}".format(k1))
    print("2.Kök: {}".format(k2))



def Tekrar():

    a = str(input("Yeniden denemek istiyorsanız (Y), Programı sonlandırmak için (S) tuşlayınız: "))
    if a == ("y"):
        Kontrol = True
    elif a == ("Y"):
        Kontrol = True

    elif a == ("S"):
        cıkıs()
    elif a == ("s"):
        cıkıs()
    else:
        print("Yanlış giriş yaptınız.\nTekrar giriniz")
        Tekrar()

def cıkıs():
    print("Programdan Çıkış yapılıyor...")
    sys.exit()
#-------------------------------- Main --------------------------------

print("""

            İkinci dereceden denklemin köklerini hesaplayan programa
                                HOŞGELDİNİZ
                                -- ***** --
                               A(x*2)+Bx+C=0


""")

A = int(0)
B = int(0)
C = int(0)
while (Kontrol == True):
    kontrol(sayıAl())
    KokBul()
    Tekrar()


