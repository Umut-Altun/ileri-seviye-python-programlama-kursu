# 2️⃣.2️⃣ List Comprehension Örnek Uygulama Soruları ve Çözümü

# ------------------------------------- LIST COMPREHENSION ÖRNEK UYGULAMA ------------------------------------------- #

# Soru 1: 1'den 100'e kadar olan sayılardan sadece çift sayıları içeren bir liste oluşturun.
# Çözüm:
# sayilar = [rakam for rakam in range(1,101) if rakam % 2 == 0]
# print(sayilar)

# Soru 2: text = "Python Öğreniyorum" Bu metindeki tüm harfleri büyük harfe çevirip listeleyelim.
# Çözüm:
# text = "Python Öğreniyorum"
# harfler = [harf.upper() for harf in text]
# print(harfler)


# Soru 3: personel_maas = [1000, 2000, 3000, 4000, 5000] Bu listedeki her personelin maaşının 3000 lira altında olup 
#   olmadığını kontrol edelim. Eger 3000 liranın altındaysa "Düşük Maaş" üstündeyse normal maasını yazdıralım.
# Çözüm:
# personel_maas = [1000, 2000, 3000, 4000, 5000]
# maaslar = [maas if maas >= 3000 else "Düşük Maaş" for maas in personel_maas ]
# print(maaslar)


# Soru 4: adlar = ["Ali", "Veli", "Ayşe"] Ve soyadlar = ["Yılmaz", "Sezer", "Kara"] Bu iki listeyi birleştirerek tüm
#  isim ve soyisimleri eşleştirerek, tam isimlere sahip bir liste oluşturalım.
# Çözüm:

adlar = ["Ali", "Veli", "Ayşe"]
soyadlar = ["Yılmaz", "Sezer", "Kara"]
tam_isimler = [adlar[index] + " " + soyadlar[index] for index in range(0, len(adlar))]
print(tam_isimler)


