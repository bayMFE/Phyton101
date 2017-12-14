import time
import random #rasgele sayı üretmemizi sağlayan modül
######################################################################
def Sor():

    a = input("Yeni oyun istiyorsanız (Y), Çıkmak için (T) tuşlayınız: ")
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
        Sor()

######################################################################
def TahminSor():
    t = int(input("Tahmininiz:"))

    if t > 50:
        print("Lütfen 1-50 aralığında bir tam sayı giriniz.")
        time.sleep(0.5)
        TahminSor()
    elif t < 1:
        print("Lütfen 1-50 aralığında bir tam sayı giriniz.")
        time.sleep(0.5)
        TahminSor()

    return t



######################################################################

def oyun(r_sayı):
    kontrol = False
    tahmin = None
    hak = 6
    while kontrol == False:

        if hak == 0:
            print("Tahmin Hakkınız dolmuştur.")
            kontrol = True

        ##################################################
        tahmin = TahminSor()

        if (tahmin < r_sayı):
            print("Tahmininizi biraz daha yükseltmelisiniz...")
            hak -= 1
            continue
        elif (tahmin > r_sayı):
            print("Tahmininizi biraz daha küçültmelisiniz...")
            hak -= 1
            continue
        elif (tahmin == r_sayı):
            print("Tebrikler Tahmin etmeyi başardınız.")
            break
######################################################################
######################################################################
#                             ANA KOD                                #
######################################################################

print("Sayı Tahmin Oyunumuza Hoşgeldiniz...")
time.sleep(1)
print("Sisteme Girişiniz sağlanıyor")
time.sleep(2)
print("\t."),time.sleep(0.5),print("\t."),time.sleep(0.5),print("\t.")
time.sleep(0.5)
TamamDevam=True
while TamamDevam == True:
    print("""
    ****************

1 ile 50 arasında bir tam sayı giriniz.

    ****************
    """)

    r_sayı = random.randint(1, 50)

    oyun(r_sayı)
    TamamDevam = Sor()


print("Programdan Çıkılıyor..."),time.sleep(1)































