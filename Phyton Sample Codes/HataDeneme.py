import os
import time
def clear_screen():
    print('\n' * 20)

while True:

    sayı1 = input("İlk sayıyı giriniz(Çıkmak için 'q' tuşuna basınız):")

    if sayı1 == "q":break

    sayı2 = input("İkinci sayıyı giriniz")

    try:
        f_sayı1 = int(sayı1)
        f_sayı2 = int(sayı2)
        print("Girilen değerlerin toplamı: {}".format(f_sayı1+f_sayı2))
    except(ValueError,ZeroDivisionError):
        print("Bir hata oluştu lütfen tekrar deneyiniz.\n\n")
        time.sleep(2)
        










