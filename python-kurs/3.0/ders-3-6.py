#3️⃣.6️⃣ Sum ve Round Fonksiyonu
#✅ Python'daki sum() fonksiyonu, bir dizi sayı veya iterable içindeki değerleri toplamak için kullanılır.
#✅ Sayısal listeler ve diziler üzerinde işlem yapar.
#✅ İsteğe bağlı olarak bir başlangıç değeri alabilir.
#✅ map(), filter() gibi fonksiyonlarla birlikte kullanılabilir.
#✅ Gerçek hayatta finans, istatistik ve veri analizinde sıkça kullanılır.
#✅ round() fonksiyonu, bir sayıyı en yakın tam sayıya veya belirli bir ondalık basamağa yuvarlamak için kullanılır.
#✅ Varsayılan olarak en yakın tam sayıya yuvarlar.

# ------------------------------------------ SUM|ROUND FONKSIYON KULLANIMI -------------------------------------------- #
# ✔ sum() Fonksiyonunun Temel Kullanımı
sayilar = [3, 5, 7, 9]
toplam = sum(sayilar)
print(toplam)

print(sum([2, 4, 6, 8, 10]))

sayilar = [10, 20, 30]
toplam = sum(sayilar, 100)  
print(toplam)

dogrular = [True, True, False, True, True, False]
sonuc = sum(dogrular)  
print(sonuc)



# ✔ sum() Fonksiyonunun map() ile Kullanımı
sayilar = [1, 2, 3, 4]
toplam = sum(map(lambda x: x**2, sayilar))  
print(toplam)

kelimeler = ["Python", "Programlama", "Dili"]
toplam_uzunluk = sum(map(len, kelimeler))  
print(toplam_uzunluk)



# ✔ round() Fonksiyonunun Temel Kullanımı
print(round(3.7)) 
print(round(3.4)) 
print(round(2.5)) 

print(round(3.14159, 2)) 
print(round(7.56789, 3))

fiyat = 49.9876
yuvarlanmis_fiyat = round(fiyat, 2)
print(yuvarlanmis_fiyat)



# ✔ Gerçek Hayatta Kullanım Senaryoları
sepet = [19.99, 5.49, 8.75, 12.99]
toplam_fiyat = sum(sepet)
yuvarlanmis_fiyat = round(toplam_fiyat, 2)

print("Toplam Fiyat:", toplam_fiyat)  
print("Yuvarlanmış Fiyat:", yuvarlanmis_fiyat) 


notlar = [75.5, 88.4, 92.3, 65.7]
ortalama = sum(notlar) / len(notlar)
print("Ortalama:", round(ortalama, 1))


notlar = [75.5, 88.4, 92.3, 65.7, 0]
puan_adeti = list(puan > 0 for puan in notlar)
print(puan_adeti)
ortalama = sum(notlar) / puan_adeti
print("Ortalama:", round(ortalama, 1))
