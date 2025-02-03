#3️⃣.2️⃣ Filter Fonksiyonu
#✅ filter() fonksiyonu, bir fonksiyonu liste veya iterable üzerine uygulayarak True dönen elemanları seçer.
#✅ Lambda fonksiyonları ile kullanımı yaygındır.
#✅ List Comprehension bazen filter() yerine daha okunaklı olabilir.
#✅ Boş metinleri temizleme, pozitif sayıları seçme gibi birçok alanda kullanılır.

# ---------------------------------------- FILTER FONKSIYON KULLANIMI ----------------------------------------------- #
# ✔ Normal Yöntem (for döngüsüyle)
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tek_sayilar = []

for sayi in sayilar:
    if sayi % 2 != 0:
        tek_sayilar.append(sayi)
print(tek_sayilar)

# ✔ Filter Kullanarak Aynı İşlem
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tek_sayilar = list(filter(lambda x: x % 2 != 0, sayilar))
print(tek_sayilar)



# ✔ Filter ile Lambda Fonksiyonlarının Kullanımı
sayilar = [-5, -2, 0, 3, 7, -8, 10]
negatif_sayilar = list(filter(lambda x: x < 0, sayilar))
print(negatif_sayilar)


kelimeler = ["Python", "ders", "ileri", "seviye", "kurs"]
uzun_kelime = list(filter(lambda x: len(x) > 5, kelimeler))
print(uzun_kelime) 


liste1 = [1, 2, 3, 4, 5, 6]
liste2 = [3, 4, 7, 8, 5]
ortak_elemanlar = list(filter(lambda x: x in liste2, liste1))
print(ortak_elemanlar) 


kelimeler = ["Python", "", " ", "Ders", "", "İleri"]
bos_olmayanlar = list(filter(lambda x: x.strip() != "", kelimeler))
print(bos_olmayanlar) 


# ✔Filter ile Normal Fonksiyon Kullanımı
def pozitif_mi(sayi):
    return sayi > 0

sayilar = [-10, -3, 0, 5, 8, -1]
pozitifler = list(filter(pozitif_mi, sayilar))
print(pozitifler)
