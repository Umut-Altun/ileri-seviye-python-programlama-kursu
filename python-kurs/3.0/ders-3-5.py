#3️⃣.5️⃣ Min ve Max Fonksiyonu
#✅ min() fonksiyonu, verilen bir iterable içindeki en küçük değeri döndürür. max() fonksiyonu, en büyük değeri döndürür.
#✅ Listeler, tuple'lar, string'ler, set'ler ve sözlükler ile kullanılabilir.
#✅ Özel sıralamalar için key parametresi ile lambda fonksiyonu kullanılabilir.
#✅ Gerçek dünyada veri analizi, sıralama ve raporlama gibi birçok alanda kullanılır.

# ------------------------------------------ MİN|MAX FONKSIYON KULLANIMI -------------------------------------------- #
# ✔ Temel Kullanımı
sayilar = [12, 5, 8, 19, 3]
print(min(sayilar))  
print(max(sayilar))  

kelime = "python"
print(min(kelime))  
print(max(kelime)) 

kelimeler = ["elma", "armut", "muz", "karpuz"]
print(min(kelimeler))  
print(max(kelimeler))



# ✔ Liste İçindeki Kullanımı
kisiler = [
    {"ad": "Ahmet", "yas": 30},
    {"ad": "Mehmet", "yas": 25},
    {"ad": "Zeynep", "yas": 35}
]
en_genc = min(kisiler, key=lambda x: x["yas"])
en_yasli = max(kisiler, key=lambda x: x["yas"])

print(en_genc)  
print(en_yasli)


urunler = [
    {"ad": "Telefon", "fiyat": 12000},
    {"ad": "Laptop", "fiyat": 25000},
    {"ad": "Tablet", "fiyat": 8000}
]
en_ucuz = min(urunler, key=lambda x: x["fiyat"])
en_pahali = max(urunler, key=lambda x: x["fiyat"])

print(en_ucuz)  
print(en_pahali) 



# ✔ Lambda ile Özelleştirilmiş Kullanım
sayilar = [-3, -1, 4, -2]
print(min(sayilar, key=lambda x: abs(x)))  # Çıktı: -1 (Mutlak değeri en küçük olan)
print(max(sayilar, key=lambda x: abs(x)))  # Çıktı: 4 (Mutlak değeri en büyük olan)



# ✔ Gerçek Hayatta Kullanım Senaryoları
hava_durumu = [
    {"gun": "Pazartesi", "sicaklik": 22},
    {"gun": "Salı", "sicaklik": 18},
    {"gun": "Çarşamba", "sicaklik": 25},
    {"gun": "Perşembe", "sicaklik": 20}
]
en_soguk_gun = min(hava_durumu, key=lambda x: x["sicaklik"])
en_sicak_gun = max(hava_durumu, key=lambda x: x["sicaklik"])

print(en_soguk_gun)
print(en_sicak_gun) 