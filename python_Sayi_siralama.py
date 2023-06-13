print("Kullanici adi:azat Sifre:dicle")
kdGirdi=input("Kullanici adini Giriniz:")
sfGirdi=input("Sifre Giriniz:")
print()
dtuser="azat"
dtsifre="dicle"
key=1
liste=[]
adet=int(input("Kac Tane Sayi Girmek isiyorsun:"))
while key<=adet:
    if dtuser==kdGirdi and sfGirdi==dtsifre:
        sayi=0
        sayi=int(input("{} Sayiyi Giriniz: ".format(key)))
        liste.append(sayi)
        key+=1
    elif sfGirdi!=dtsifre and dtuser!=kdGirdi:
        print("Girilen bilgiler tamami ile yanlis :(")
        break
    elif dtuser!=kdGirdi:
        print("Kullanici adi yanlis :(")
        break
    elif sfGirdi!=dtsifre:
        print("Sifre yanlis :(")
        break
    
liste.sort()
print("Girdiginiz sayilarin kucukten buyuye siralanmasi {}".format(liste))
liste.reverse()
print("Girdiginiz sayilarin buyukten kuçuge siralanmasi {}".format(liste))
