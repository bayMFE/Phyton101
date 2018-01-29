#Developed by bayMFE

import math
import sys

global A,B,C,k1,k2
Kontrol = True

#-------------------------------- CLASS --------------------------------
class fonk():

    def sıfırla(self):
        global A,B,C
        A = int(0)
        B = int(0)
        C = int(0)

    def sayıAl(self):
        global A, B, C

        A = int(0)
        B = int(0)
        C = int(0)
        while True:
            try:
                A = int(input("Lütfen A katsayısını giriniz: "))
                B = int(input("Lütfen B katsayısını giriniz: "))
                C = int(input("Lütfen C katsayısını giriniz: "))
            except ValueError:
                print("Lütfen sadece tamsayı giriniz.\nKatsayılar adı üzerinde sayılardan oluşur!!!\n")
                continue
            break

    def KokBul(self):
        global A, B, C, k1, k2
        k1 = int(0)
        k2 = int(0)
        delta = (B * B) - (4 * A * C)

        if (delta > 0):
            k1 = (((B ** 2) - math.sqrt(delta)) / (2 * A))
            k2 = (((B ** 2) + math.sqrt(delta)) / (2 * A))
            fonk.KokYaz(self)

        elif (delta == 0):
            k1 = (-B) / (2 * A)
            k2 = k1
            fonk.KokYaz(self)

        else:
            print("Denklemin kökleri imajinerdir.")

    def KokYaz(self):
        global k1, k2
        print("1.Kök: {}".format(k1))
        print("2.Kök: {}".format(k2))

    def Tekrar(self):

        a = str(input("Yeniden denemek istiyorsanız (Y), Programı sonlandırmak için (S) tuşlayınız: "))
        if a == ("y"):
            Kontrol = True
        elif a == ("Y"):
            Kontrol = True

        elif a == ("S"):
            fonk.cıkıs(self)
        elif a == ("s"):
            fonk.cıkıs(self)
        else:
            print("Yanlış giriş yaptınız.\nTekrar giriniz")
            fonk.Tekrar(self)

    def cıkıs(self):
        print("Programdan Çıkış yapılıyor...")
        sys.exit()


    def welcome(self):
        print("""
        
                    İkinci dereceden denklemin köklerini hesaplayan programa
                                        HOŞGELDİNİZ
                                        -- ***** --
                                       A(x*2)+Bx+C=0
        
        
        """)
#-------------------------------- CLASS --------------------------------
def main():
    app = fonk()
    app.welcome()
    while (Kontrol == True):
        app.sıfırla()
        app.sayıAl()
        app.KokBul()
        app.Tekrar()

if __name__=="__main__":
  main()


