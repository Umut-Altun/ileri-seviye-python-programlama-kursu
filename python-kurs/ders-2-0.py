# 2️⃣.0️⃣ List Comprehension Nedir?
# Python'da listeleri oluşturmanın kısa ve etkili bir yoludur.
# Döngülerle liste oluşturmak yerine daha okunaklı ve hızlı bir yöntem sunar.
# Daha Kısa Kod: Tek satırda liste oluşturabiliriz.
# Daha Okunabilir: Döngülerden daha sade ve anlaşılır olabilir.
# Daha Hızlı: Python’un dahili optimizasyonlarından faydalanır.

# ---------------------------------------- LIST COMPREHENSION KULLANIM ----------------------------------------------- #
# for item in liste:
#     expression


# [expression for item in liste]

# rakamlar =[]
# for i in range(1,10):
#     rakamlar.append(i)

# print(rakamlar)

# rakamlar = [i for i in range(1,10)]
# print(rakamlar)


# rakamlar =[]
# for i in range(1,10):
#     rakamlar.append(i ** 2)

# print(rakamlar)

# rakamlar = [rakam ** 2 for rakam in range(1,10)]
# print(rakamlar)


# urunler = ["elma", "armut","kıraz"]
# buyuk_harfli_urunler =[]
# for urun in urunler:
#     buyuk_harfli_urunler.append(urun.upper())

# print(urunler)
# print(buyuk_harfli_urunler)

# urunler = ["elma", "armut","kıraz","vısne"]
# buyuk_harfli_urunler = [ urun.upper() for urun in urunler]
# print(buyuk_harfli_urunler)
