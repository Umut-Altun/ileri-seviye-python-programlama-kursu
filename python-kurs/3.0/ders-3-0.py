#3️⃣.0️⃣ Lambda ve Builtin Fonksiyonlar Nedir
#✅ Lambda fonksiyonları, tek satırda tanımlanan ve isme ihtiyaç duymayan küçük fonksiyonlardır.
#✅ def ile oluşturulan fonksiyonların daha kısa bir alternatifidir.
#✅ Tek kullanımlık küçük fonksiyonlar için idealdir.
#✅ Built-in fonksiyonlarla kullanılarak kodu kısaltır.
#✅ Map, Filter, Sorted gibi fonksiyonlarla birlikte sıkça kullanılır.

# ---------------------------------------- LAMBDA FONKSIYON KULLANIMI ----------------------------------------------- #
# ✔ Normal Fonksiyon:
# def fonksiyonAdı(arguments):
    # expressıon
    
# ✔ Lambda ile Aynı İşlem:
# lamba arguments: expressıon


def yasHesapla(dogumTarihi):
    return (2025 - dogumTarihi)
ali = yasHesapla(1990)
print(ali)

yasHesapla = lambda dogumTarihi: 2025 - dogumTarihi
ali = yasHesapla(1990)
print(ali)

ali = (lambda dogumTarihi: 2025 - dogumTarihi)(1990)
print(ali)



def maasHesapla(maas1,maas2,maas3):
    return ( (maas1+maas2+maas3) / 3 )
ort_maas = maasHesapla(2000,4000,3500)
print(ort_maas)

ort_maas2 = lambda maas1,maas2,maas3: ((maas1+maas2+maas3) / 3)
print(ort_maas2(350,500,900))

ali_maas = (lambda maas1,maas2,maas3: ((maas1+maas2+maas3) / 3))(2000,5600,450)
print(ali_maas)



def maasZam(maas):
    return (lambda zam: zam + maas)
personel_1 = maasZam(2000)(330)
print(personel_1)


def maasZam(maas):
    return (lambda zam: zam + maas)
personel_1 = maasZam(2000)
sonuc = personel_1(590)
print(sonuc)



# ********************************************* Builtin Fonksiyonlar ************************************************* #
# ✔ Matematiksel Fonksiyonlar:
print(abs(-10))  # 10
print(pow(2, 3))  # 8 (2^3)
print(round(3.14159, 2))  # 3.14

# ✔ Tür Dönüşüm Fonksiyonları:
print(int("10"))  # 10
print(float("3.14"))  # 3.14
print(str(100))  # '100'

# ✔ Toplama ve Sıralama Fonksiyonları:
sayilar = [3, 7, 1, 9, 2]
print(sum(sayilar))  # 22
print(min(sayilar))  # 1
print(max(sayilar))  # 9
print(sorted(sayilar))  # [1, 2, 3, 7, 9]


# ✔ Herhangi Bir Elemanın Doğru Olup Olmadığını Kontrol Eden Fonksiyonlar:
liste = [False, False, True, False]
print(any(liste))  # True (çünkü en az bir eleman True)

liste = [True, True, True]
print(all(liste))  # True (çünkü tüm elemanlar True)


# ✅ Kullanıcıdan Alınan Girdiyi Temizleme
girdi = "  Python Kursu  "
temizlenmis = girdi.strip().lower()
print(temizlenmis)  # "python kursu"
