#3️⃣.3️⃣ Ayn ve All Fonksiyonu
#✅ any() ve all() fonksiyonları, bir iterable içinde bulunan True ve False değerlerini değerlendirerek bir sonuç döndürür.
#✅ any() fonksiyonu, iterable içindeki en az bir eleman True ise True döndürür.
#✅ all() fonksiyonu, iterable içindeki tüm elemanlar True ise True döndürür.
#✅ Boş iterable için any() False, all() True döndürür.
#✅ Gerçek hayatta form kontrolleri, kullanıcı aktivasyonu gibi birçok alanda kullanılır.


# Kullanım -----------------any()---------all()-----
# Tüm elemanlar True	    ✅ True	    ✅ True
# En az bir eleman True	    ✅ True	    ❌ False
# Tüm elemanlar False	    ❌ False	    ❌ False
# Boş Liste	                ❌ False	    ✅ True

# ------------------------------------------ ANY|ALL FONKSIYON KULLANIMI -------------------------------------------- #
# ✔ Temel Kullanım
liste = [False, False, True, False]
print(any(liste))

liste = [True, True, True]
print(all(liste))


# ✔ Boş bir liste için
print(any([]))
print(all([]))


# ✔ Liste içindeki sayılar ile kullanım
sayilar = [0, 0, 5, 0]
print(any(sayilar))

sayilar = [5, 10, 3, 0]
print(all(sayilar))


# ✔ Bir kelimenin içinde belirli bir harfin olup olmadığını kontrol etme
kelime = "Python"
harfler = ["a", "b", "o"]
print(any(harf in kelime for harf in harfler)) 

kelime = "Python123"
print(all(harf.isalpha() for harf in kelime))



# ✔ Any ve All ile Lambda Kullanımı
sayilar = [1, 3, 5, 8]
print(any(map(lambda x: x % 2 == 0, sayilar)))

sayilar = [2, 4, 6, 8]
print(all(map(lambda x: x % 2 == 0, sayilar)))



# ✔ Gerçek Hayatta Any ve All Kullanımı
form_bilgileri = ["Ahmet", "Kaya", "", "ahmet@example.com"]
eksik_var_mi = any(bilgi == "" for bilgi in form_bilgileri)
print(eksik_var_mi)


kullanicilar = [
    {"ad": "Ali", "aktif": True},
    {"ad": "Mehmet", "aktif": True},
    {"ad": "Ayşe", "aktif": False}
]

hepsi_aktif_mi = all(kullanici["aktif"] for kullanici in kullanicilar)
print(hepsi_aktif_mi) 