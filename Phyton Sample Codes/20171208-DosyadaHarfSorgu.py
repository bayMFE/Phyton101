

#Okuma yapacak olduğunuz dosyanın .py uzantılı kod dosyasının bulunduğu klasörde olması gerekmektedir.
hakkında = open("Dosya.txt", "r" ) # "Dosya.txt" ifadesi dosyanın adına göre değiştirilmelidir.
                                   # "r" txt dosyasını okuma modunda oçma işlevi görmektedir.

harf = input("Sorgulamak istediğiniz harfi giriniz: ")

sayı = 0

for karakter_dizisi in hakkında:
    for karakter in karakter_dizisi:
        if harf == karakter:
            sayı += 1
print(sayı)
hakkında.close()


