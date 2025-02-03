#3️⃣.1️⃣ Map Fonksiyonu
#✅ map() fonksiyonu, bir fonksiyonu bir iterable (dizi, liste, tuple, vs.) üzerinde çalıştırarak yeni bir iterable oluşturur.
#✅ map() fonksiyonu, listedeki her elemanı belirli bir fonksiyondan geçirerek işlem yapar.
#✅ Lambda fonksiyonlarıyla birlikte kullanıldığında çok daha pratik hale gelir.

# ---------------------------------------- MAP FONKSIYON KULLANIMI ----------------------------------------------- #
# ✔ Normal Yöntem (for döngüsüyle)
sayilar = [1, 2, 3, 4, 5]
kareler = []
for sayi in sayilar:
    kareler.append(sayi ** 2)

print(kareler)


# ✔ Map Kullanarak Aynı İşlem
def kareAl(sayi):
    return sayi ** 2

sayilar = [1, 2, 3, 4, 5]
kareler = map(kareAl, sayilar)    #list(map(kareAl, sayilar))
print(kareler)


# ✔ Lambda ve Map Kullanarak Aynı İşlem
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda sayi: sayi ** 2, sayilar))
print(kareler)  



# ✔ Hazır Fonksiyonlarla Map Kullanımı
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(str, sayilar))
print(kareler)  

sira_sayilari = ["1", "2", "3", "4", "5"]
rakamlar = list(map(int, sayilar))
print(rakamlar)  



# ✔ Map ve Lambda Kullanım Senaryoları
kelimeler = ["python", "kursu", "ileri", "seviye"]
buyuk_harf = list(map(lambda kelime: kelime.upper(), kelimeler))
print(buyuk_harf)


personeller = [
    {"ad":"umut", "soyad":"altun", "yas":"25"},
    {"ad":"dogan", "soyad":"demir", "yas":"55"},
    {"ad":"sude", "soyad":"gul", "yas":"30"},
]
sonuc = list(map(lambda personel_ad: personel_ad["ad"] , personeller))
print(sonuc)  


kurslar = ["Django", "Flask", "FastAPI"]
yeni_kurslar = list(map(lambda x: "Python - " + x, kurslar))
print(yeni_kurslar)


liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
toplam = list(map(lambda x, y: x + y, liste1, liste2))
print(toplam)
