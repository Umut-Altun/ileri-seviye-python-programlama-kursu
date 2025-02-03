#3️⃣.4️⃣ Sorted Fonksiyonu
#✅ sorted() fonksiyonu iterable nesneleri sıralar ve yeni bir liste döndürür.
#✅ Varsayılan olarak küçükten büyüğe sıralama yapar, ters sıralama için reverse=True kullanılır.
#✅ key parametresi ile özel sıralamalar yapılabilir.
#✅ Sözlükler, tuple'lar ve set'ler üzerinde de kullanılabilir.
#✅ Gerçek dünyada veritabanı sıralamaları, dosya yönetimi gibi alanlarda kullanılır.

# ------------------------------------------ SORTED FONKSIYON KULLANIMI -------------------------------------------- #
# ✔ Temel Kullanımı
sayilar = [5, 2, 9, 1, 7]
print(sorted(sayilar))  

harfler = ["z", "c", "a", "m"]
print(sorted(harfler))  

kelimeler = ["elma", "armut", "üzüm", "muz"]
print(sorted(kelimeler))  

sayilar = [10, 3, 5, 2]
print(sorted(sayilar, reverse=True))  



# ✔ key Parametresi ile Özelleştirilmiş Sıralama
kelimeler = ["elma", "armut", "karpuz", "kivi"]
print(sorted(kelimeler, key=len))  

kelimeler = ["Zeytin", "üzüm", "Armut", "elma", "zencefil"]
print(sorted(kelimeler, key=str))  



# ✔ Lambda ile Kullanım
sayilar = [-3, -1, 4, -2]
print(sorted(sayilar, key=lambda x: x**2))  

kelimeler = ["elma", "armut", "karpuz", "muz"]
print(sorted(kelimeler, key=lambda x: x[-1]))  



# ✔ Tuple ve Set Gibi Veri Tipleriyle Kullanım
tup = (5, 2, 8, 1)
print(sorted(tup))  

kume = {4, 1, 7, 2}
print(sorted(kume))  



# ✔ Liste İçindeki Sözlükleri Sıralama
kisiler = [
    {"ad": "Ahmet", "yas": 30},
    {"ad": "Mehmet", "yas": 25},
    {"ad": "Zeynep", "yas": 35}
]

sirali = sorted(kisiler, key=lambda x: x["yas"])
print(sirali)

sirali_isimler = sorted(kisiler, key=lambda x: x["ad"])
print(sirali_isimler)


# ✔ Gerçek Hayatta Kullanım Senaryoları
kullanicilar = [
    {"ad": "Ali", "puan": 85},
    {"ad": "Veli", "puan": 90},
    {"ad": "Ayşe", "puan": 58},
    {"ad": "Fatma", "puan": 98},
    {"ad": "Hakan", "puan": 78},
]

en_yuksek_puan = sorted(kullanicilar, key=lambda x: x["puan"], reverse=True)
print(en_yuksek_puan)