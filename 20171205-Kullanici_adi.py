

print("Sisteme Hoşgeldiniz...\n")

kontrol = False
sayac =0

while kontrol == False:
    sayac = sayac+1
    if(sayac==4):
        print("3 hatalı girişte bulundunuz. Sistemden çıkışınız gerçekleştiriliyor.\n")
        break
    k_adi = input("Kullanıcı adı: ")

    sifre = input("Şifre: ")

    if (k_adi == "baymfe" and sifre == 1234):
        print("Sisteme girişiniz onaylandı...")
        kontrol = True
    elif(len(k_adi)+len(sifre)<3 or len(k_adi)+len(sifre)>20):
        print("Amacın ne genç ??\nTekrar dene...\n\n")
    elif (k_adi != "baymfe" or sifre != 1234):
        print("Kullanıcı adı veya Şifreniz yanlış.\nLütefen tekrar deneyiniz...\n")





